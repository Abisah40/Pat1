from django.contrib import admin
from .models import ContactForm
# Register your models here.

admin.site.register(ContactForm)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','address','message','created_at')
    list_filter = ('created')
    search_fields = ('name','phone','created_at')
