from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User , Address

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Personal info", {"fields": ["fullname"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["username", "email"]
    ordering = ["username"]
    filter_horizontal = []




admin.site.register(User, UserAdmin)
admin.site.register(Address)

