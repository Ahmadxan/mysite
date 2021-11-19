from django.contrib import admin
from . import forms, models
from django.contrib.auth.admin import UserAdmin
from .models import Contact


class CustomUserAmin(UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.CustomUser

    list_display = ["username", 'email', 'first_name', 'last_name', 'age', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(models.CustomUser, CustomUserAmin)
admin.site.register(Contact)
