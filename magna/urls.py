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
    path("submit-absence-request/", forms.views.submit_absence_request, name='submit_absence_request'),
    path("requests", forms.views.requests, name="requests"),
    path('api/allowed-absent/', forms.views.allowed_absent_data, name='allowed-absent-data'),
    path('api/days-requested/', forms.views.days_requested_data, name='days-requested-data'),
    path('api/update-allowed-absent/', forms.views.update_allowed_absent, name='update-allowed-absent'),
    path("calendar", forms.views.calendar, name="calendar"),
    path("", workflows.views.view_workflows, name='list'),
    path("", workflows.views.edit_workflow, name='edit'),
    path("", workflows.views.delete_workflow, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
