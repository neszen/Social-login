from django.urls import path 
from . import views 
urlpatterns = [
    path("checkout_session",views.checkout_session,name='checkout_session'),
    path("create_checkout_session",views.create_checkout_session,name='create_checkout_session'),
    path('stripe_webhook',views.stripe_webhook, name='stripe_webhook'),
    path("success/",views.success,name='success'),
    path("cancel",views.cancel,name='cancel'),
]
