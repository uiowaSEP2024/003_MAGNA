from django.test import TestCase
from django.urls import reverse


class LoginTestCase(TestCase):
    def test_login_page(self):
        """FILL IN"""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_login_form(self):
        """FILL IN"""
        # Add a test for form submission here
        pass
