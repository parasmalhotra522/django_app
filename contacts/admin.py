from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    # this is to show the fields in the admin section these all fields wll be displayed
    # in the admin section
    list_display = ('id', 'name', 'listing', 'email','contact_date')
    list_display_links = ('id', 'listing') # this is that the fields which will be clickable
    list_filter = ('contact_date', 'listing',) # these are to add filtering feature
    # list_editable = ('is_published', )
    search_fields = ('listing_id', 'name', 'listing', 'email', 'phone', 'user_id', 'contact_date')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)