from django.db import models
from appProduct.models import Product



class Carousel(models.Model):
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   image = models.ImageField(("Carousel Resmi"), upload_to='carousel', max_length=500)
   title = models.CharField(("Carousel Başlığı"), max_length=450)

   def __str__(self):
      return self.product.title
