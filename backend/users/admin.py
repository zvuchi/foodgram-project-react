from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class BaseAdminSettings(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_filter = ('email', 'username')


class UsersAdmin(UserAdmin):
    list_display = (
        'id',
        'role',
        'username',
        'email',
        'first_name',
        'last_name'
    )
    list_display_links = ('id', 'username')
    search_fields = ('role', 'username')


admin.site.register(User, UsersAdmin)
