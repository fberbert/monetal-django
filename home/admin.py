from django.contrib import admin
from .models import OnePage

@admin.register(OnePage)
class OnePageAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_name', 'active', 'show_menu')
    ordering = ['order']


#admin.site.register(OnePage, OnePageAdmin)
