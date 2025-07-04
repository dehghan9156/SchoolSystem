from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from accounts.models import * 

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['pk','name','family','role','confirmation']
    fieldsets = (
        ("Authentication", {"fields": ("username", "password","codemeli","role")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "is_superuser")},
        ),
        ("Group Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important Date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )



admin.site.register(User,CustomUserAdmin)