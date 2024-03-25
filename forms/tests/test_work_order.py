from django.test import TestCase, RequestFactory
from django.urls import reverse
from forms.models import WorkOrder
from forms.views import submit_work_order
from django.http import HttpRequest
from django.contrib.messages import get_messages


class WorkOrderTests(TestCase):
    def test_valid_form_submission(self):
        # Setting up the data for the test
        form_data = {
            "order_number": "123",
            "shift_number": "1",
            "department_affected": "Production",
            "full_name": "John Doe",
            "machine_affected": "Machine 1",
            "boolean_var1": 'true',
            "boolean_var2": 'false',
            "boolean_var3": 'true',
            "boolean_var4": 'false',
            "work_type": "Repair",
            "requested_date": "2022-01-01",
            "operation_affected": "Operation 1",
            "email": "john.doe@example.com",
            "describe_problem": "Machine is not working properly",
            "root_cause": "Faulty sensor",
            "work_requested": "Replace sensor"
        }

        # Making a POST request to the view
        response = self.client.post(reverse('submit-work-order'), data=form_data)

        # Verifying that a WorkOrder object was created
        work_order = WorkOrder.objects.get(order_number="123")
        self.assertEqual(work_order.shift_number, "1")
        self.assertEqual(work_order.department_affected, "Production")
        # Continue with other assertions...

        # Check if the response redirects to the work_order.html page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "work_order.html")

        # Check if the success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Work order submitted successfully.")

