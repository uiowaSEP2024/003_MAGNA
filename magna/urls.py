"""
URL configuration for magna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

import forms.views
import home.views
import login.views
import workflows.views

urlpatterns = [
    path("admin/", admin.site.urls),
    # root view
    path("", login.views.login_view, name="login"),
    path("home", home.views.index, name="home"),
    path("absence-request", forms.views.absence_request, name="absence-request"),
    path("work-order", forms.views.work_order, name="work-order"),
    path("workflow", workflows.views.workflows, name="workflow"),
    path("submit-absence-request/", forms.views.submit_absence_request, name="submit_absence_request"),
    path("submit-work-order/", forms.views.submit_work_order, name="submit-work-order"),
    path("view_job_postings/", forms.views.view_job_postings, name="view_job_postings"),
    path("create_job_postings/", forms.views.create_job_postings, name="create_job_postings"),
    path("upload_pdf/", forms.views.upload_pdf, name="upload_pdf"),
    path('create_pdf_content/', forms.views.create_pdf_from_content, name='create_pdf_content'),
    path("requests", forms.views.requests, name="requests"),
    path("api/allowed-absent/", forms.views.allowed_absent_data, name="allowed-absent-data"),
    path("search-requests/", forms.views.search_requests, name="search-requests"),
    path(
        "api/allowed-absent/",
        forms.views.allowed_absent_data,
        name="allowed-absent-data",
    ),
    path(
        "api/days-requested/",
        forms.views.days_requested_data,
        name="days-requested-data",
    ),
    path(
        "api/update-allowed-absent/",
        forms.views.update_allowed_absent,
        name="update-allowed-absent",
    ),
    path("calendar", forms.views.calendar, name="calendar"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("travel-auth", forms.views.travel_auth_form),
    path('workflows/time-off/', workflows.views.manage_email_recipients, {'form_type': 'time_off'}, name='manage_time_off_recipients'),
    path('workflows/job-postings/', workflows.views.manage_email_recipients, {'form_type': 'job_postings'}, name='manage_job_postings_recipients'),
    path('workflows/work-orders/', workflows.views.manage_email_recipients, {'form_type': 'work_orders'}, name='manage_work_orders_recipients'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
