from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin 

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    # Specify the fields to be displayed on the user list page
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active')
    
    # Specify the fields to be used for searching users
    search_fields = ('username', 'email')

    # Specify the fields to be displayed on the user detail page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define which fields will be used in the "add user" form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff'),
        }),
    )
    
    # Set the ordering of users in the admin list
    ordering = ('username',)


# Register the custom User model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
