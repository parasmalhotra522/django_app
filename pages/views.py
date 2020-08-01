from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = { 'listings' : listings,'state_choices':state_choices,
    'bedroom_choices':bedroom_choices, 'price_choices':price_choices }

    return render(request, 'pagestemplate/index.html', context)

def aboutus(request):
    realtors = Realtor.objects.order_by('-hire_date')
    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {'realtors':realtors, 'mvp_realtors':mvp_realtors}    
    return render(request, 'pagestemplate/about.html', context)