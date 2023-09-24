from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account
from .forms import AccountCreationForm, AccountChangeForm


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',
                    'is_active', 'modified_date', 'created_date')
    readonly_fields = ('last_login', 'modified_date', 'created_date')
    list_filter = ('created_date', 'is_superuser', 'is_staff', 'is_active')
    date_hierarchy = 'created_date'
    ordering = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('modified_date', 'created_date')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2'), }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(Account, AccountAdmin)