from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'created_at')
    search_fields = ('email','username', 'first_name', 'last_name')
    ordering = ('-created_at',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info',{'fields': ('phone','avatar', 'bio', 'github_profile','linkedin_profile','portforlio_url')}),
        ('Statistics',{'fields': ('total_documents','total_questions','is_verified')}),
    )
    

   
