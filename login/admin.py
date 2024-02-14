from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


# Register your models here.

# A default Admin grabbed from chatgpt for now - this is by no means final. Edit as you see fit.
class EmployeeAdmin(UserAdmin):
    model = Employee
    # Optionally customize the fields to be displayed in the admin interface
    list_display = ['email', 'name', 'role', 'is_staff', 'is_active', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'clock_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'clock_number',)}),
    )


admin.site.register(Employee, EmployeeAdmin)
