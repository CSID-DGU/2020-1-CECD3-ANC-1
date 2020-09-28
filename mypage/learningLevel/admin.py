from django.contrib import admin
from .models import *

# Register your models here.

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')


admin.site.register(AuthUser, AuthUserAdmin)