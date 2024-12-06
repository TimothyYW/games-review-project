from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Review

class ReviewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.review = Review.objects.create(
            user=self.user,
            title='Test Review',
            game_name='Test Game',
            review='Test content',
            image='path/to/test/image.jpg',
            image_alt='Test image',
            type_game='single_player',
            genre='action',
            developer='Test Developer'
        )

    def test_review_creation(self):
        self.assertEqual(self.review.title, 'Test Review')
        self.assertEqual(self.review.user, self.user)

    def test_review_list_view(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_review_detail_view(self):
        response = self.client.get(
            reverse('review_detail', kwargs={'pk': self.review.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_detail.html')
