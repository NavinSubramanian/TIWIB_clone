from django.contrib import admin
from .models import *
# Register your models here.
class WebpageAdmin(admin.ModelAdmin):
    list_display=('name','type','photo','description')


class ContentAdmin(admin.ModelAdmin):
    list_display=('name','type','typ2','pic','des','rate','link')
    search_fields=Content.SearchableFields


class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','type','message')

class UserAdmin(admin.ModelAdmin):
    list_display=('name','password')

admin.site.register(Webpage,WebpageAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(User,UserAdmin)