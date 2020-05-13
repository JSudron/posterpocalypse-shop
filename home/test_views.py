from django.test import TestCase

class TestHomeViews(TestCase):


    def test_home_template(self):
        page = self.client.get('/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('index.html')


    def test_about_template(self):
        page = self.client.get('/about')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('about.html')


    def test_contact_info_template(self):
        page = self.client.get('contact.html')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('contact.html')
