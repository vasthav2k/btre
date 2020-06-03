from django.shortcuts import  redirect, render
from django.contrib import messages
from .models import Query
from django.core.mail import send_mail
# Create your views here.
def query(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        # Check if user has made an inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Query.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You\'ve already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)


        query=Query(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        query.save()

        #send email

        send_mail(
            'Property Listing Enquiry',
            'Hey there,' + '\n'+ 'There has been a inquiry for '+listing + 'from ' + name +'. Sign into the admin panel for more info',
            from_email='vasthav2000@gmail.com',
            recipient_list= [realtor_email,'vasthav1729@gmail.com'],
            fail_silently=False
        )

        # send_mail('Property Enquiry',
        # 'There is client for you','vasthav2000@gmail.com',
        # recipient_list=['vasthav1729@gmail.com'],fail_silently=False
        # )

        messages.success(request,'Your request has been submitted successfully ,a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)