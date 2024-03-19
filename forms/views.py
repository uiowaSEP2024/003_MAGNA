import json
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import AbsenceRequest, AbsentDaysAllowed, JobPDFs, WorkOrder
from .forms import PDFUploadForm

# Create your views here.


def calendar(request):
    """
    Renders the calendar page.

    Args:
    - request: the HTTP request object

    Returns:
    - Rendered calendar.html template
    """
    return render(request, "calendar.html")


def home_page(request):
    """
    Renders the home page.

    Args:
    - request: the HTTP request object

    Returns:
    - Rendered home.html template
    """
    return render(request, "home.html")


def absence_request(request):
    """
    Renders the absence_request page.

    Args:
    - request: the HTTP request object

    Returns:
    - Rendered absence_request.html template
    """
    return render(request, "absence_request.html")


def work_order(request):
    """
    Renders the absence_request page.

    Args:
    - request: the HTTP request object

    Returns:
    - Rendered work_order.html template
    """
    return render(request, "work_order.html")


def requests(request):
    """
    View function to render the requests.html template with a list of all active absence requests.
    Args:
    - request: the HttpRequest object representing the request made to the server.
    Returns:
    - HttpResponse object with the rendered HTML content.
    """
    activeRequests = AbsenceRequest.objects.all()
    return render(request, "requests.html", {"requests": activeRequests})


def view_job_postings(request):
    pdfs = JobPDFs.objects.all()
    return render(request, 'view_job_postings.html', {'pdfs': pdfs})


def create_job_postings(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_pdf = UploadedPDF(
                title=form.cleaned_data['title'],
                pdf_file=request.FILES['pdf_file']
            )
            new_pdf.save()
            # Redirect to PDF list or success page
            return redirect('list_pdfs')
    else:
        form = PDFUploadForm()
    return render(request, 'create_job_postings.html', {'form': form})

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "PDF uploaded successfully.")
            return redirect('view_job_postings')  # or wherever you want to redirect after upload
    else:
        form = PDFUploadForm()
    return render(request, 'create_job_postings.html', {'form': form})

def submit_absence_request(request):
    """
    Process the form submission for absence request.
    Args:
    request: the HTTP request object
    Returns:
    HTTP response object
    """
    """
    Process the submission of the absence request form.
    Validates the form data, saves a new AbsenceRequest object, sends a confirmation email to the user,
    and redirects to the list of requests on success. Shows an error message on invalid form submission.
    """
    if request.method == "POST":
        # Extract form data
        clock_number = request.POST.get("clock_number")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        shift_number = request.POST.get("shift_number")
        email = request.POST.get("email")
        hours_gone = request.POST.get("hours_gone")
        absence_type = request.POST.get("absence_type")

        # Check if required fields are present
        if (
            start_date
            and end_date
            and shift_number
            and hours_gone
            and absence_type
            and clock_number
            and email
        ):
            # Create and save the AbsenceRequest object
            absence_request = AbsenceRequest(
                clock_number=clock_number,
                start_date=start_date,
                end_date=end_date,
                approval_status="pending",  # Default to 'pending' as approval is not instant
                shift_number=shift_number,
                email_address=email,
                hours_gone=hours_gone,
                absence_type=absence_type,
                # Omit the 'approval' and 'filled_by' fields until log in feature fully implemented
            )
            absence_request.save()
            messages.success(request, "Request submitted successfully.")

            subject = "Absence Request Submitted"
            message = f"Your absence request from {start_date} to {end_date} has been submitted and is pending approval."
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email_address],  # noqa: F821
                fail_silently=False,
            )
            messages.success(request, "Request submitted successfully.")
            return redirect("requests")
        else:
            # Handle the invalid form case
            messages.error(request, "Invalid form submission.")

    return render(request, "absence_request.html")


def submit_work_order(request):
    """
    Process the form submission for work order.
    Args:
    request: the HTTP request object
    Returns:
    HTTP response object
    """
    if request.method == "POST":
        # Extract form data
        order_number = request.POST.get("order_number")
        shift_number = request.POST.get("shift_number")
        department_affected = request.POST.get("department_affected")
        full_name = request.POST.get("full_name")
        machine_affected = request.POST.get("machine_affected")
        quality_issue = request.POST.get("boolean_var1") == 'true'
        safety_issue = request.POST.get("boolean_var2") == 'true'
        planned = request.POST.get("boolean_var3") == 'true'
        sensor_issue = request.POST.get("boolean_var4") == 'true'
        work_type = request.POST.get("work_type")
        requested_date = request.POST.get("requested_date")
        operation_affected = request.POST.get("operation_affected")
        email = request.POST.get("email")
        describe_problem = request.POST.get("describe_problem")
        root_cause = request.POST.get("root_cause")
        work_requested = request.POST.get("work_requested")

        # Check if required fields are present
        if (
            order_number
            and shift_number
            and department_affected
            and full_name
            and machine_affected
            and work_type
            and operation_affected
            and email
            and describe_problem
            and root_cause
            and work_requested
        ):
            # Create and save the WorkOrder object
            work_order = WorkOrder(
                order_number=order_number,
                shift_number=shift_number,
                department_affected=department_affected,
                full_name=full_name,
                machine_affected=machine_affected,
                quality_issue=quality_issue,
                safety_issue=safety_issue,
                planned=planned,
                sensor_issue=sensor_issue,
                work_type=work_type,
                requested_date=requested_date,
                operation_affected=operation_affected,
                email=email,
                describe_problem=describe_problem,
                root_cause=root_cause,
                work_requested=work_requested,
            )
            work_order.save()
            messages.success(request, "Work order submitted successfully.")
            # Redirect to an appropriate page
            return render(request, "work_order.html")
        else:
            # Handle the invalid form case
            messages.error(request, "Invalid form submission.")

    return render(request, "work_order.html")


def allowed_absent_data(request):
    """
    Retrieve all AbsentDaysAllowed objects and return the data as JSON response.
    Args:
    request: the HTTP request object
    Returns:
    JsonResponse: a JSON response containing the data of all AbsentDaysAllowed objects
    """
    data = AbsentDaysAllowed.objects.all().values("shiftDay", "allowedAbsent")
    return JsonResponse(list(data), safe=False)


def days_requested_data(request):
    """
    Retrieve all dates requested in absence requests that have not been rejected.

    Args:
    - request: HTTP request object

    Returns:
    - JSON response containing all the requested dates
    """
    all_dates = []

    # Retrieve absence requests that are not rejected
    absence_requests = AbsenceRequest.objects.exclude(approval_status="rejected")

    # Iterate through each absence request and retrieve all dates within the request period
    for request in absence_requests:
        start_date = request.start_date
        end_date = request.end_date
        delta = end_date - start_date

        for i in range(delta.days + 1):
            day = start_date + timedelta(days=i)
            all_dates.append(day.strftime("%Y-%m-%d"))

    return JsonResponse(all_dates, safe=False)


@require_POST
def update_allowed_absent(request):
    """
    Update the allowed number of absent days for a specific shift day.
    Parameters:
    - request: the HTTP request containing the shift day and allowed absent data in JSON format
    Returns:
    - JsonResponse: a JSON response indicating the status of the update
    """
    try:

        # Parse the request body as JSON
        data = json.loads(request.body)

        # Convert the shift day string to a datetime object
        shift_day = datetime.strptime(data["shiftDay"], "%Y-%m-%d").date()

        # Retrieve the allowed absent value
        allowed_absent = int(data["allowedAbsent"])

        # Update or create the AbsentDaysAllowed object for the specified shift day
        obj, created = AbsentDaysAllowed.objects.update_or_create(
            shiftDay=shift_day, defaults={"allowedAbsent": allowed_absent}
        )

        return JsonResponse({"status": "success"})
    except Exception as e:

        # Handle any exceptions and return an error response
        return JsonResponse({"status": "error", "message": str(e)})



