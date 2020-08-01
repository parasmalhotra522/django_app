from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    # this is to show the fields in the admin section these all fields wll be displayed
    # in the admin section
    list_display = ('id', 'title', 'is_published', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # this is that the fields which will be clickable
    list_filter = ('realtor', 'price',) # these are to add filtering feature
    list_editable = ('is_published', )
    search_fields = ('description', 'title', 'city', 'price', 'address', 'state', 'zipcode')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)
