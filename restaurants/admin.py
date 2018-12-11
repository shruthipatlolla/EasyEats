from django.contrib import admin
from restaurants.models import Food


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [('Description', {'fields': ['name', 'desc', 'menu']}),
                 ('Address', {'fields': ['address', 'post_code', 'town']}),
                 ('Contact', {'fields': ['web', 'gmap_url', 'phone']}),
                 ('Food', {'fields': ['food']}),
                 ('Pictures', {'fields': ['picture', 'map']}), ]


admin.site.register(Food)