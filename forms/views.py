from django.shortcuts import render, redirect
from .models import AbsenceRequest
from django.contrib import messages


# Create your views here.
def home_page(request):
    """FILL IN"""
    return render(request, "home.html")


def absence_request(request):
    """FILL IN"""
    return render(request, "absence_request.html")


def requests(request):
    """FILL IN"""
    return render(request, "requests.html")

def submit_absence_request(request):
    if request.method == "POST":
        # Create an instance of your model and save the form data
        absence_request = AbsenceRequest(
            start_date=request.POST.get('first_day_absent'),
            end_date=request.POST.get('last_day_absent'),
            approval_status="pending",  # Set default status as pending
            shift_number=request.POST.get('shift'),
            hours_gone=request.POST.get('hours'),
            absence_type=request.POST.get('absence_type'),
            # Assuming `approval` and `filled_by` should be set based on the logged-in user or some other logic
            # approval= ... ,
            # filled_by= ... ,
            clock=request.POST.get('clock'),
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
        )
        absence_request.save()
        messages.success(request, 'Request submitted successfully.')
        return redirect('view-requests')

    return render(request, 'absence_request.html')

def view_requests(request):
    requests = AbsenceRequest.objects.all()
    return render(request, 'requests.html', {'requests': requests})