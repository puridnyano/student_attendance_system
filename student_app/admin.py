from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(CustomUser)
class adminclass(admin.ModelAdmin):
    list_display = ['id','username','base_role']

@admin.register(Student)
class studentclass(admin.ModelAdmin):
    list_display = ['id','username','base_role']

@admin.register(Teacher)
class teacherclass(admin.ModelAdmin):
    list_display = ['id','username','base_role']



