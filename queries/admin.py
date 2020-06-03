from django.contrib import admin
from .models import Query
# Register your models here.

class QueryAdmin(admin.ModelAdmin):
    list_display=['id','name','listing','email','contact_date']
    list_display_links=['id','name']
    search_fields=['email','name','listing']
    list_per_page=25



admin.site.register(Query,QueryAdmin)
