from django.test import TestCase

class TestViewWorkflows:

    #  Returns a HTTP response with status code 200.
    def test_returns_http_response_with_status_code_200(self):
        response = self.client.get('/view_workflows/')
        assert response.status_code == 200

    #  No workflows exist in the database.
    def test_no_workflows_exist_in_database(self):
        Workflow.objects.all().delete()
        response = self.client.get('/view_workflows/')
        assert response.status_code == 200
        assert len(response.context['workflows']) == 0

class TestEditWorkflow:

    #  The function should retrieve the Workflow object with the given primary key.
    def test_retrieve_workflow(self):
        # Arrange
        request = None
        pk = 1

        # Act
        result = edit_workflow(request, pk)

        # Assert
        assert result == get_object_or_404(Workflow, pk=pk)

    #  If the Workflow object with the given primary key does not exist, the function should return a 404 error.
    def test_nonexistent_workflow(self):
        # Arrange
        request = None
        pk = 999

        # Act
        with pytest.raises(Http404):
            edit_workflow(request, pk)


class TestDeleteWorkflow:

    #  Deletes a workflow when a POST request is received
    def test_delete_workflow_post_request(self):
        # Create a mock request object with method set to POST
        request = type('Request', (object,), {'method': 'POST'})

        # Create a mock workflow object
        workflow = type('Workflow', (object,), {'delete': lambda: None})

        # Mock the get_object_or_404 function to return the mock workflow object
        with patch('path.to.get_object_or_404', return_value=workflow):
            # Call the delete_workflow function with the mock request object and a valid pk
            response = delete_workflow(request, 1)

            # Assert that the workflow.delete() method was called
            workflow.delete.assert_called_once()

            # Assert that the response is a redirect to the 'workflows:list' URL
            assert response.url == 'workflows:list'

    #  Returns a 404 error if the workflow with the given pk does not exist
    def test_delete_workflow_invalid_pk(self):
        # Create a mock request object with method set to POST
        request = type('Request', (object,), {'method': 'POST'})

        # Mock the get_object_or_404 function to raise a 404 error
        with patch('path.to.get_object_or_404', side_effect=Http404):
            # Call the delete_workflow function with the mock request object and an invalid pk
            response = delete_workflow(request, 999)

            # Assert that the response status code is 404
            assert response.status_code == 404

class TestManagerReview:

    #  The function correctly retrieves the absence request object with the given primary key and 'submitted' workflow status.
    def test_retrieve_absence_request(self):
        # Arrange
        request = HttpRequest()
        request.method = 'GET'
        pk = 1
        absence_request = AbsenceRequest.objects.create(pk=pk, workflow__status='submitted')

        # Act
        response = manager_review(request, pk)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['absence_request'], absence_request)

    #  The absence request object with the given primary key does not exist, and a 404 error is raised.
    def test_absence_request_not_found(self):
        # Arrange
        request = HttpRequest()
        request.method = 'GET'
        pk = 1

        # Act
        with self.assertRaises(Http404):
            manager_review(request, pk)


class TestHrReview:

    #  Renders the 'workflows/review.html' template with the 'absence_request' object as context when the request method is GET
    def test_renders_template_with_context(self):
        # Arrange
        request = RequestFactory().get('/')
        absence_request = AbsenceRequest.objects.create(pk=1, workflow__status='manager_review')

        # Act
        response = HR_review(request, 1)

        # Assert
        assert response.status_code == 200
        assert response.template_name == 'workflows/review.html'
        assert response.context_data['absence_request'] == absence_request

    #  Returns a 404 response if the 'AbsenceRequest' object with the given 'pk' does not exist
    def test_returns_404_if_absence_request_does_not_exist(self):
        # Arrange
        request = RequestFactory().get('/')

        # Act
        response = HR_review(request, 1)

        # Assert
        assert response.status_code == 404
