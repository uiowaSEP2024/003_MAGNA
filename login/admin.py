from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Employee


class EmployeeAdmin(UserAdmin):
    """Customize the Employee model for the admin interface."""

    model = Employee
    # Optionally customize the fields to be displayed in the admin interface
    list_display = [
        "username",
        "name",
        "role",
        "is_staff",
        "is_active",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "clock_number", "name")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "clock_number", "name")}),
    )


admin.site.register(Employee, EmployeeAdmin)


