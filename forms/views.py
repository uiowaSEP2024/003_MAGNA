from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from forms.forms import PTOForm


# Create your views here.
def home_page(request):
    """FILL IN"""
    return render(request, "home.html")


def pto(request):
    if request.method == 'POST':
        form = PTOForm(request.POST)
        if form.is_valid():
            request_form = authenticate(clock=form.cleaned_data['clock'],
                                        shift=form.cleaned_data['shift'],
                                        name=form.cleaned_data['full-name'],
                                        first_day_absent=form.cleaned_data['first-day-absent'],
                                        last_day_absent=form.cleaned_data['last-day-absent'],
                                        hours=form.cleaned_data['hours'],
                                        absent_type=form.cleaned_data['absence-type'],
                                        approving_supervisor=form.cleaned_data['approving-supervisor'],
                                        email=form.cleaned_data['email'])
            if request_form is not None:
                # test print statement please remove before deployment
                print("Form valid")
                return redirect('home')
    else:
        form = PTOForm()
    return render(request, 'pto.html', {'form': form})
