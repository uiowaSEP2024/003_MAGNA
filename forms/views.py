from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render

from .models import AbsenceRequest


# Create your views here.
def home_page(request):
    """Render the home page of the web application."""
    return render(request, "home.html")


def absence_request(request):
    """Display the absence request form to the user."""
    return render(request, "absence_request.html")


def requests(request):
    """Display a list of all active absence requests to the user."""
    activeRequests = AbsenceRequest.objects.all()
    return render(request, "requests.html", {"requests": activeRequests})


def submit_absence_request(request):
    """
    Process the submission of the absence request form.
    Validates the form data, saves a new AbsenceRequest object, sends a confirmation email to the user,
    and redirects to the list of requests on success. Shows an error message on invalid form submission.
    """
    if request.method == "POST":
        # Extract form data
        s_date = request.POST.get("first_day_absent")
        e_date = request.POST.get("last_day_absent")
        shift_number = request.POST.get("shift")
        hours_gone = request.POST.get("hours")
        absence_type = request.POST.get("absence_type")
        email_address = request.POST.get("email")

        # Check if required fields are present

        if s_date and e_date and shift_number and hours_gone and absence_type:
            # Create and save the AbsenceRequest object
            absence_request = AbsenceRequest(
                start_date=s_date,
                end_date=e_date,
                approval_status="pending",  # Default to 'pending'
                shift_number=shift_number,
                hours_gone=hours_gone,
                absence_type=absence_type,
            )
            absence_request.save()

            subject = "Absence Request Submitted"
            message = f"Your absence request from {start_date} to {end_date} has been submitted and is pending approval."
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email_address],
                fail_silently=False
            )
            messages.success(request, "Request submitted successfully.")
            return redirect("requests")
        else:
            # Handle the invalid form case
            messages.error(request, "Invalid form submission.")
            return render(request, "absence_request.html")

    return render(request, "absence_request.html")
