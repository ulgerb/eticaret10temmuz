"""
URL configuration for eticaret10temmuz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *
from appProduct.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexPage ,name='indexPage'),
    path('contact', contactPage,name='contactPage'),
    path('detail/<slug>', detailPage,name='detailPage'),
    path('likeComment/<user>/<productslug>', likeComment,name='likeComment'),
    path('summary', summaryPage,name='summaryPage'),
    path('summaryDelete/<sbid>', summaryDelete,name='summaryDelete'),
    path('product', productPage,name='productPage'),
    path('productShopAdd/<pid>', productShopAdd,name='productShopAdd'),
    
    # USER
    
    path('logoutUser/logoutUser', logoutUser,name='logoutUser'),
    path('login', loginPage,name='loginPage'),
    path('register', registerPage,name='registerPage'),
    path('passwordChange',passwordChangePage ,name='passwordChangePage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
