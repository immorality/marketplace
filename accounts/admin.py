from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomAccountCreationForm, CustomAccountChangeForm
from .models import CustomAccount

class CustomAccountAdmin(UserAdmin):
    fieldsets = (
    (None, {'fields': ('username', 'email', 'password', 'is_seller')}),
    ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active',)}),
    )
    
    add_form = CustomAccountCreationForm
    form = CustomAccountChangeForm
    model = CustomAccount
    list_display = ['email', 'username', 'is_seller']


admin.site.register(CustomAccount, CustomAccountAdmin)