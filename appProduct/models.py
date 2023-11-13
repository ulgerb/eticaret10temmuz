from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Color(models.Model):
   title = models.CharField(("Renkler"), max_length=50)
   title_code = models.CharField(("Renk Kodu"), max_length=50, null=True)
   
   def __str__(self):
      return self.title
   
class Product(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Ürün Başlık"), max_length=50)
   price = models.FloatField(("Ürün Fiyat"))
   stok = models.IntegerField(("Stok"))
   text = models.TextField(("Açıklama"))
   color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
   slug = models.SlugField(("Slug"))
   
   def save(self):
      self.slug = slugify(self.title)
      super().save()

      
   def __str__(self):
      return self.title
   
   
class ProductImage(models.Model):
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   image = models.ImageField(("Resim"), upload_to="product", max_length=300)

   def __str__(self):
      return self.product.title

   
class Comment(models.Model):
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,related_name="user")
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   text = models.TextField(("Yorum"))
   like = models.ManyToManyField(User, verbose_name=("Beğenen Kullanıcı"),related_name="like")
   
   def __str__(self):
      return self.product.title
   
   
class ShopBasket(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   quanity = models.IntegerField(("Adet"), default=0)
   total_price = models.FloatField(("Toplam Fiyat"), default=0)
   
   def __str__(self):
      return self.product.title