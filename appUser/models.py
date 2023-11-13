from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   birthdate = models.DateField(("Doğum Tarihi"), auto_now_add=False)
   address1 = models.TextField(("Adres 1"))
   address2 = models.TextField(("Adres 2"))
   city = models.CharField(("Şehir"), max_length=50)
   mobile = models.CharField(("Telefon"), max_length=50)

   def __str__(self):
      return self.user.username