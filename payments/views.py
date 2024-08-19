import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from decimal import Decimal
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_API_KEY
DOMAIN = settings.DOMAIN

def checkout_session(request):
    if request.method == 'POST':
        try:
            # Get the product details from the POST request
            product_name = request.POST.get('name')
            product_price = Decimal(request.POST.get('price')) * 100  # Convert to cents for Stripe
            product_description = request.POST.get('description')

            user_email = request.user.email  

            # Create a Stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': int(product_price),  # Stripe requires the price in cents
                            'product_data': {
                                'name': product_name,
                                'description': product_description,
                                'images': ['https://images.unsplash.com/photo-1579202673506-ca3ce28943ef'],
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                billing_address_collection='required',
                success_url=DOMAIN + '/success',
                cancel_url=DOMAIN + '/cancel',
                customer_email=user_email,
            )
            
            return redirect(checkout_session.url)
        except Exception as error:
            return render(request, 'public/error.html', {'error': error})

    return render(request, 'public/cancel.html')


def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')





def create_checkout_session(request):
    if request.method == 'POST':
        try:
            productId = request.POST.get('productId')
         
            user_email = request.user.email    
            checkout_session = stripe.checkout.Session.create(

                line_items=[
                    {
                        'price': productId ,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                billing_address_collection='required',
                success_url=DOMAIN + '/success',
                cancel_url=DOMAIN + '/cancel',
                customer_email=user_email,
                metadata={
                'plan_id': productId,
                }
            )
            
            return redirect(checkout_session.url)
        except Exception as error:
          
            return render (request,'public/error.html',{'error':error})

    return render(request, 'public/cancel.html')




@csrf_exempt 
def stripe_webhook(request):
  
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.WEBHOOK_ENDPOINT_SECRET
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError :
        return HttpResponse(status=400)

   
    if event['type'] == 'checkout.session.completed' :
        print(event)
        print('Payment was successful.') 
      

    
    return HttpResponse(status=200)






