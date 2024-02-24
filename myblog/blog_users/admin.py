from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'middle_name','contact_no')

admin.site.register(BlogUser, CustomUserAdmin)