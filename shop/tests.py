# Create your tests here.
# tests.py inside shop or backendApp app

from django.test import TestCase
from .models import Product, Review
from django.contrib.auth.models import User


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.review = Review.objects.create(
            user=self.user, product=self.product, rating=4)

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 4)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        self.product = Product.objects.create(name="Test Product", price=100)

    # Ensure the user is logged in correctly before making the GET request


def test_product_detail_view(self):
    # Log the user in
    self.client.login(username="testuser", password="12345")

    # Fetch the product detail page
    response = self.client.get(f'/shop/product/{self.product.id}/')

    # Check if the status code is 200
    self.assertEqual(response.status_code, 200)
    # Ensure the product detail is rendered
    self.assertContains(response, "Test Product")

   # Check that the review post request works and that the review is created


def test_review_post(self):
    # Log the user in
    self.client.login(username="testuser", password="12345")

    # Submit a review
    response = self.client.post(f'/shop/product/{self.product.id}/add_review/', {
        'rating': 5,
        'comment': 'Great product!'
    })

    # Check that the response redirects (assuming it does on success)
    self.assertEqual(response.status_code, 302)

    # Check that the review was created
    self.assertTrue(Review.objects.filter(
        product=self.product, rating=5).exists())
