import datetime

import pytest
from django.core.exceptions import ValidationError

from forms.models import JobPDFs
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from forms.forms import PDFUploadForm
from forms.forms import PDFContentForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from django.urls import reverse
from forms.views import create_job_postings, view_job_postings, upload_pdf, create_pdf_from_content
from django.test import RequestFactory



@pytest.mark.django_db
class TestCreateJobPostings:
    def test_create_job_postings(self):
        request = RequestFactory().get('/create_job_postings/')
        response = create_job_postings(request)
        assert response.status_code == 200

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

        # Check if the response status code is 200 indicating rendering instead of redirect
        assert response.status_code == 200

    def test_no_search_query_or_sort_order(self):
        request = RequestFactory().get('/')
        response = view_job_postings(request)
        assert response.status_code == 200
        # Assuming 'view_job_postings.html' lists PDFs, adjust the text to match actual content
        assert b'PDFs' in response.content

    def test_no_matching_search_query(self):
        request = RequestFactory().get('/', {'search_query': 'nonexistent'})
        response = view_job_postings(request)
        assert response.status_code == 200

    def test_invalid_data_submission(self):
        # Simplified setup for POST request with invalid file
        request = RequestFactory().post('/upload_pdf', {'file': ''}, format='multipart')

        # Call the upload_pdf function
        response = upload_pdf(request)

        # Assert that the response is not a redirect
        assert response.status_code != 302

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