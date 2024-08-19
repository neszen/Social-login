
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('user.urls')),
    path("",include('allauth.urls')),
    path("",include('shop.urls')),
    path("",include('payments.urls'))

]
