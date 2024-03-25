import datetime

import pytest
from django.core.exceptions import ValidationError

from forms.models import JobPDFs

from forms.views import create_job_postings, view_job_postings, upload_pdf, create_pdf_from_content
from django.test import RequestFactory

@pytest.mark.django_db
class TestCreateJobPostings:
    @pytest.mark.django_db
    def test_valid_form_data(self):
        # Initialize form data
        form_data = {
            'title': 'Test Job Posting',
            'pdf_file': 'test.pdf'
        }

        # Create a request object with POST method and valid form data
        request = RequestFactory().post('/create_job_postings/', data=form_data)

        # Call the create_job_postings function
        response = create_job_postings(request)

        # Check if the response redirects to the correct page
        assert response.status_code == 302
        assert response.url == 'list_pdfs'

        # Check if a new PDF object is created with the correct data
        new_pdf = UploadedPDF.objects.get(title='Test Job Posting')
        assert new_pdf.title == 'Test Job Posting'
        assert new_pdf.pdf_file.name == 'test.pdf'

    def test_invalid_form_data(self):
        # Initialize form data with missing required fields
        form_data = {
            'title': '',
            'pdf_file': ''
        }

        # Create a request object with POST method and invalid form data
        request = RequestFactory().post('/create_job_postings/', data=form_data)

        # Call the create_job_postings function
        response = create_job_postings(request)

        # Check if the response renders the create_job_postings.html template
        assert response.status_code == 200
        assert response.template_name == 'create_job_postings.html'

        # Check if the form is not valid and contains errors
        form = response.context_data['form']
        assert not form.is_valid()
        assert form.errors != {}

    def test_no_search_query_or_sort_order(self):
        request = RequestFactory().get('/')
        response = view_job_postings(request)
        assert response.status_code == 200
        assert response.template_name == 'view_job_postings.html'
        assert 'pdfs' in response.context
        assert 'sort_order' in response.context

    def test_no_matching_search_query(self):
        request = RequestFactory().get('/', {'search_query': 'nonexistent'})
        response = view_job_postings(request)
        assert response.status_code == 200
        assert response.template_name == 'view_job_postings.html'
        assert 'pdfs' in response.context
        assert 'sort_order' in response.context
        assert len(response.context['pdfs']) == 0

    def test_valid_data_submission(self):
        from django.http import HttpRequest
        from django.test import RequestFactory
        from django.contrib.messages.storage.fallback import FallbackStorage

        # Create a request object
        request = HttpRequest()
        request.method = 'POST'
        request.FILES = {'file': 'test.pdf'}

        # Create a request factory and attach the request to it
        factory = RequestFactory()
        request = factory.post('/upload_pdf', {'file': 'test.pdf'})
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        # Call the upload_pdf function
        response = upload_pdf(request)

        # Assert that the response is a redirect
        assert response.status_code == 302
        assert response.url == 'view_job_postings'

    def test_invalid_data_submission(self):
        from django.http import HttpRequest
        from django.test import RequestFactory
        from django.contrib.messages.storage.fallback import FallbackStorage

        # Create a request object
        request = HttpRequest()
        request.method = 'POST'
        request.FILES = {'file': ''}

        # Create a request factory and attach the request to it
        factory = RequestFactory()
        request = factory.post('/upload_pdf', {'file': ''})
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        # Call the upload_pdf function
        response = upload_pdf(request)

        # Assert that the response is not a redirect
        assert response.status_code != 302
        assert response.url != 'view_job_postings'

    def test_generate_pdf_with_labels(self):
        # Set up test data
        request = RequestFactory().post('/create_pdf', {
            'title': 'Test PDF',
            'textInputLabels[]': ['Label 1', 'Label 2'],
            'checkboxLabels[]': ['Checkbox 1', 'Checkbox 2']
        })

        # Call the function under test
        response = create_pdf_from_content(request)

        # Assert that the response is a redirect
        assert isinstance(response, HttpResponseRedirect)

        # Assert that a PDF file was created and saved
        assert JobPDFs.objects.filter(title='Test PDF').exists()

    def test_generate_pdf_without_labels(self):
        # Set up test data
        request = RequestFactory().post('/create_pdf', {
            'title': 'Test PDF',
            'textInputLabels[]': [],
            'checkboxLabels[]': []
        })

        # Call the function under test
        response = create_pdf_from_content(request)

        # Assert that the response is a redirect
        assert isinstance(response, HttpResponseRedirect)

        # Assert that a PDF file was created and saved
        assert JobPDFs.objects.filter(title='Test PDF').exists()