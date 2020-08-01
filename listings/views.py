from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
# Create your views here.
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.choices import state_choices, bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
     # this is to fetch the data from the database and show only the listings which are published

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    

    context = { 'listings' : paged_listings }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    #urllist = [1,2,3,4,5,6]#['photo_1', 'photo_2','photo_3','photo_4','photo_5','photo_6']
    context = { 'listing': listing  }
    return render(request, 'listings/listing.html', context)    

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # we are matching for similarity of the keywords in the description
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # we are now matching for exact city name and passing them as query
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)
    
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {'state_choices':state_choices,
    'bedroom_choices':bedroom_choices, 'price_choices':price_choices, 
    'listings': queryset_list,
    'values' : request.GET
    
     }
    return render(request, 'listings/search.html', context)
