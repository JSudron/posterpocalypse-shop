from unittest import mock
from accounts.models import Customer
from django.contrib.auth import get_user_model
from django.test import TestCase
from products.models import Product


class TestView(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "test", "test@gmail.com", "test"
        )
        Customer.objects.create(user=self.user)


    def test_checkout(self):
        self.client.login(username="test", password="test")
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)


    def test_shipping(self):
        page = self.client.get("/checkout/shipping/")
        self.assertEqual(page.status_code, 302)
    

    def test_order_history(self):
        page = self.client.get("/checkout/order_history/")
        self.assertEqual(page.status_code, 200)


    def test_checkout_payment_with_valid_credentials(self):
        self.client.login(email='test@gmail.com', password='password')
        page = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '111',
            'expiry_month': '7',
            'expiry_year': '2021',
            'stripe_id': 'tok_visa',
        })

        self.assertTrue(page.status_code, 200)


    def test_checkout_payment_with_declined_card(self):
        self.client.login(email='test@gmail.com', password='password')
        page = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '111',
            'expiry_month': '7',
            'expiry_year': '20251',
            'stripe_id': 'tok_chargeDeclined',
        }, follow=True)

        self.assertTemplateNotUsed('order_success.html')
