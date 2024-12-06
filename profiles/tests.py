from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm

class ProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = Profile.objects.get(user=self.user)
        self.test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertTrue(hasattr(self.profile, 'image'))
        self.assertTrue(hasattr(self.profile, 'bio'))

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_view(self):
        response = self.client.get(
            reverse('profile', kwargs={'pk': self.user.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_edit_profile_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('edit_profile', kwargs={'pk': self.profile.id}),
            {'bio': 'New bio content'}
        )
        self.assertEqual(response.status_code, 302)
        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.bio, 'New bio content')

    def test_edit_profile_unauthenticated(self):
        response = self.client.post(
            reverse('edit_profile', kwargs={'pk': self.profile.id}),
            {'bio': 'New bio content'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/profiles/edit/{self.profile.id}')

    def test_edit_profile_wrong_user(self):
        self.client.login(username='testuser2', password='testpass123')
        response = self.client.post(
            reverse('edit_profile', kwargs={'pk': self.profile.id}),
            {'bio': 'New bio content'}
        )
        self.assertEqual(response.status_code, 302)
