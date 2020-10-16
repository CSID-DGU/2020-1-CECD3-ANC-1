from django.contrib import admin
from .models import *

# Register your models here.

class MdlUserAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'firstname', 'lastname', 'email')

class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'start', 'end')

admin.site.register(MdlUser, MdlUserAdmin)
admin.site.register(HomeWork, HomeWorkAdmin)
admin.site.register(MdlRoleAssignments)