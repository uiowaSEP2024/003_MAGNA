from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class FormsTestCase(TestCase):

    def test_pto_page(self):
        response = self.client.get(reverse('pto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pto.html')

    #still needs a test for the pto form submission here
    def test_pto_submit(self):
        pass
