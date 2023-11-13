from .models import ShopBasket

def shopBasketInfo(request):

   if request.user.is_authenticated: # girişliyse

      shopbasket_list = ShopBasket.objects.filter(user=request.user)
      totalproductprice = 0
      totalkdv = 0
      totalkargo = 0
      for i in shopbasket_list:
         totalproductprice += i.total_price
         totalkdv += i.total_price * 0.08
         totalkargo += (0 if i.total_price >= 500 else  15)

      totalprice = totalproductprice + totalkdv + totalkargo
      context = {
         "shopbasket_list": shopbasket_list,
         "totalprice": totalprice,
      }
      return context

