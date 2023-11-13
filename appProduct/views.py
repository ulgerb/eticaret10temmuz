from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def detailPage(request, slug):
   product = Product.objects.get(slug=slug)
   comments = Comment.objects.filter(product=product)

   
   if request.method == "POST":
      submit = request.POST.get("submit")
      if submit == "commentSubmit":
         if not Comment.objects.filter(user=request.user, product=product).exists():
            text = request.POST.get("text")
            comment = Comment(text=text, product=product, user=request.user)
            comment.save()
         else:
            messages.error(request, "Zaten bir yorum yazmışsınız!!")

      elif submit == "commentUpdateSubmit":
         text = request.POST.get("text")
         comment = Comment.objects.get(user=request.user, product=product)
         comment.text = text
         comment.save()
      elif submit == "addShopSubmit":
         quanity = request.POST.get("quanity") 
         
         if 5 >= int(quanity) >= 1:
            if ShopBasket.objects.filter(product=product, user=request.user).exists(): # eklenen ürün daha önceden sepette var mı?
               shopbasket = ShopBasket.objects.filter(product=product, user=request.user).first() # sepetteki ürün
               if (int(shopbasket.quanity) + int(quanity)) <= int(product.stok):
                  shopbasket.quanity = int(shopbasket.quanity) + int(quanity) # önceki adetle ilave ettiği adeti topla
                  shopbasket.total_price = int(shopbasket.quanity) * float(product.price) # toplam sepet adetiyle fiyatı çarp
                  shopbasket.save()
               else:
                  messages.error(request, f"en fazla {int(product.stok)-int(shopbasket.quanity)} ürün ekleyebilirsiniz!")

            else: # hiç ürün yoksa
               if int(quanity) <= int(product.stok):
                  totalprice = float(product.price) * int(quanity)
                  shopbasket = ShopBasket(user=request.user, product=product, quanity=quanity, total_price=totalprice )
                  shopbasket.save() 
               else:
                  messages.error(request, f"en fazla {int(product.stok)} ürün ekleyebilirsiniz!")
                  

         
      return redirect("detailPage", slug=slug)
     
         
   context={
      "product":product,
      "comments":comments,
   }
   return render(request,'product_details.html', context)


@login_required(login_url="loginUser")
def likeComment(request, user, productslug):
   comment = Comment.objects.get(user__username = user, product__slug= productslug)

   if request.user in comment.like.all():
      comment.like.remove(request.user)
   else:
      comment.like.add(request.user)
   return redirect("detailPage", slug=productslug)
   
@login_required(login_url="loginUser")
def summaryPage(request):

   shopbasket_list = ShopBasket.objects.filter(user=request.user)
   totalproductprice = 0
   totalkdv = 0
   totalkargo = 0
   for i in shopbasket_list:
      totalproductprice += i.total_price
      totalkdv += i.total_price * 0.08
      totalkargo += (0 if i.total_price >= 500 else  15)

   totalprice = totalproductprice + totalkdv + totalkargo
   
   if request.method == "POST":
      quanity_list = request.POST.getlist("quanity")
      for i in range(len(shopbasket_list)): 
         if 5 >= int(quanity_list[i]) >= 1: 
            if int(quanity_list[i]) <= int(shopbasket_list[i].product.stok):
               shopbasket_list[i].quanity = quanity_list[i]
               shopbasket_list[i].total_price = float(shopbasket_list[i].product.price) * int(shopbasket_list[i].quanity) 
               shopbasket_list[i].save()
            else:
               messages.error(request, f"en fazla {int(shopbasket_list[i].product.stok)} ürün alabilirsiniz!")
            
         
      return redirect("summaryPage")
   
   context={
      "shopbasket_list":shopbasket_list,
      "totalprice":totalprice,
      "totalproductprice":totalproductprice,
      "totalkdv":totalkdv,
      "totalkargo":totalkargo,
   }
   return render(request,'product_summary.html', context)

@login_required(login_url="loginUser")
def summaryDelete(request, sbid):
   shopbasket = ShopBasket.objects.get(user=request.user, id = sbid)
   shopbasket.delete()
   return redirect("summaryPage")

   

def productPage(request):
   product_list = Product.objects.all()
   
   context={
      "product_list":product_list,
   }
   return render(request,'products.html', context)

@login_required(login_url="loginUser")
def productShopAdd(request, pid):

   product = Product.objects.get(id=pid)

   if ShopBasket.objects.filter(user=request.user, product=product).exists(): # ürün sepette var mı yok mu?
      shopbasket = ShopBasket.objects.filter(user=request.user, product=product).first()
      if (int(shopbasket.quanity) + 1) <= int(product.stok):
         shopbasket.quanity = int(shopbasket.quanity) + 1
         shopbasket.total_price = float(shopbasket.total_price) * int(shopbasket.quanity)
         shopbasket.save()
      else:
         messages.error(request, f"en fazla {int(product.stok)-int(shopbasket.quanity)} ürün ekleyebilirsiniz!")
   else: # ürün sepette ekli değilse
      if product.stok > 0:
         shopbasket = ShopBasket(user=request.user, product=product, quanity=1, total_price = product.price )
         shopbasket.save()
      else:
         messages.error(request, f"Ürün stokta kalmamıştır!")
         
   
   return redirect("productPage")