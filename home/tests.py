from django.test import TestCase
from django.urls import reverse
from .models import Review

class IndexViewTests(TestCase):
    def test_index_view_with_no_reviews(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No reviews are available.")
        self.assertQuerysetEqual(response.context['reviews'], [])

    def test_index_view_with_reviews(self):
        Review.objects.create(title="Test Review", content="Test content")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['reviews'],
            ['<Review: Test Review>']
        )
