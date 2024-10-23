# Create your tests here.
# tests.py inside shop or backendApp app

from django.test import TestCase
from .models import Product, Review
from django.contrib.auth.models import User


# class ProductModelTest(TestCase):
#     def setUp(self):
#         self.product = Product.objects.create(name="Test Product", price=100)

#     def test_product_creation(self):
#         self.assertEqual(self.product.name, "Test Product")
#         self.assertEqual(self.product.price, 100)


# class ReviewModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username="testuser")
#         self.product = Product.objects.create(name="Test Product", price=100)
#         self.review = Review.objects.create(
#             user=self.user, product=self.product, rating=4)

#     def test_review_creation(self):
#         self.assertEqual(self.review.rating, 4)


# class ViewsTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username="testuser", password="12345")
#         self.client.login(username="testuser", password="12345")
#         self.product = Product.objects.create(name="Test Product", price=100)

#     # Ensure the user is logged in correctly before making the GET request


# def test_product_detail_view(self):
#     # Log the user in
#     self.client.login(username="testuser", password="12345")

#     # Fetch the product detail page
#     response = self.client.get(f'/shop/product/{self.product.id}/')

#     # Check if the status code is 200
#     self.assertEqual(response.status_code, 200)
#     # Ensure the product detail is rendered
#     self.assertContains(response, "Test Product")

#    # Check that the review post request works and that the review is created


# def test_review_post(self):
#     # Log the user in
#     self.client.login(username="testuser", password="12345")

#     # Submit a review
#     response = self.client.post(f'/shop/product/{self.product.id}/add_review/', {
#         'rating': 5,
#         'comment': 'Great product!'
#     })

#     # Check that the response redirects (assuming it does on success)
#     self.assertEqual(response.status_code, 302)

#     # Check that the review was created
#     self.assertTrue(Review.objects.filter(
#         product=self.product, rating=5).exists())


def calculate_accuracy():
    reviews = Review.objects.all()

# Ground truth labels
    true_labels = []
    for review in reviews:
        if(review.isFake ==  True):
            true_labels.append(True)
        else:
            true_labels.append(False)
    # true_labels = [review.isFake for review in reviews]
    predictions = []

    threshold = 0.5  # Example threshold for fake review detection

    for review in reviews:
        if float(review.polarity.to_decimal()) < threshold:
            predictions.append(True)  # Predicted as fake
        else:
            predictions.append(False)  # Predicted as real

    correct = 0
    for i in range(len(reviews)):
        if predictions[i] == true_labels[i]:
            correct += 1

    accuracy = correct / len(reviews) * 100
    return accuracy


# Output accuracy
print(f"Accuracy: {calculate_accuracy():.2f}%")
