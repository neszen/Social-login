from django.urls import path 
from . import views 
urlpatterns = [

    path("products",views.products,name='products'),
    path("subscription",views.subscription,name='subscription'),

]