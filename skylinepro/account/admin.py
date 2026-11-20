from django.contrib import admin
from .models import User

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)