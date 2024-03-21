from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AbsentDaysAllowed
from .models import AbsenceRequest

# Register your models here.

# Will need to add once admin and sign in is all complete
# admin.site.register(AbsentDaysAllowed)

# class AbsenceRequestAdmin(UserAdmin):
#     model = AbsenceRequest
#
#     list_display = [
#         "clock_number",
#         "start_date",
#         "filled"
#     ]
