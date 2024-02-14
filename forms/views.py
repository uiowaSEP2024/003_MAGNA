from django.shortcuts import render, redirect
from .models import AbsenceRequest
from django.contrib import messages
from django.http import JsonResponse
from .models import AbsentDaysAllowed


# Create your views here.

def calendar(request):
    """FILL IN"""
    return render(request, "calendar.html")


def home_page(request):
    """FILL IN"""
    return render(request, "home.html")


def absence_request(request):
    """FILL IN"""
    return render(request, "absence_request.html")


def requests(request):
    activeRequests = AbsenceRequest.objects.all()
    return render(request, 'requests.html', {'requests': activeRequests})

def submit_absence_request(request):
    if request.method == "POST":
        # Extract form data
        start_date = request.POST.get('first_day_absent')
        end_date = request.POST.get('last_day_absent')
        shift_number = request.POST.get('shift')
        hours_gone = request.POST.get('hours')
        absence_type = request.POST.get('absence_type')

        # Check if required fields are present
        if start_date and end_date and shift_number and hours_gone and absence_type:
            # Create and save the AbsenceRequest object
            absence_request = AbsenceRequest(
                start_date=start_date,
                end_date=end_date,
                approval_status="pending",  # Default to 'pending'
                shift_number=shift_number,
                hours_gone=hours_gone,
                absence_type=absence_type,
                # Omit the 'approval' and 'filled_by' fields if not logged in or not applicable
            )
            absence_request.save()
            messages.success(request, 'Request submitted successfully.')
            return redirect('requests')
        else:
            # Handle the invalid form case
            messages.error(request, 'Invalid form submission.')
            return render(request, 'absence_request.html')

    return render(request, 'absence_request.html')

def allowed_absent_data(request):
    data = AbsentDaysAllowed.objects.all().values('shiftDay', 'allowedAbsent')
    return JsonResponse(list(data), safe=False)

