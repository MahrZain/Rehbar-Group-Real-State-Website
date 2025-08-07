from django.contrib import admin
from .models import Home, About, Contact, ContactInfo, SocialMedia, Service, client,Feature
# Register your models here.
admin.site.register(Home)
admin.site.register(About)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
admin.site.register(Contact,ContactAdmin)
admin.site.register(ContactInfo)
admin.site.register(SocialMedia)
admin.site.register(Service)
admin.site.register(client)
admin.site.register(Feature)