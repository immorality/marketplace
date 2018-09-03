from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import Account

class AccountAdmin(UserAdmin):
    
    model = Account
    add_form = AccountCreationForm
    form = AccountChangeForm
    list_display = ['email', 'username', 'seller', 'date_joined']

    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('username', 'password1', 'password2', 'seller', 'first_name'),
        }),
    )

admin.site.register(Account, AccountAdmin)