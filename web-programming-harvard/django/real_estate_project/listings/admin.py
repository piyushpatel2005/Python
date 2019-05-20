from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin)


admin.site.register(Listing)
