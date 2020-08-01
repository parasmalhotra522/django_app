from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contacts(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if the user has already contacted for the same listing
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id) 
            if has_contacted:
                messages.error(request,"You have already inquired for the same query")
                return redirect('/listings/'+ listing_id)
        contact = Contact(listing=listing,listing_id=listing_id,
        name=name, email=email, phone=phone, message=message,
        user_id=user_id)
        contact.save()

        # sending mail to the user for the mail
        send_mail(
            'Property Listing Enquiry',
            'There has been an enquiry for '+ listing + '. Sign into admin panel for more info',
            'encodeproject0001@gmail.com',
            [realtor_email, 'parasmalhotra522@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your response has been submitted , We will get back to you soon!')
        return redirect('/listings/'+ listing_id) 
    else:
        return redirect('index') 
     

# Create your views here.
