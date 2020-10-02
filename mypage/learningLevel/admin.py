from django.contrib import admin
from .models import *

# Register your models here.

class MdlUserAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'firstname', 'lastname', 'email')

admin.site.register(MdlUser, MdlUserAdmin)