from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='username', email='useremail@mail.com', password='password'
        )
        self.url = reverse('board:home')

    def test_home_view_load(self):
        self.client.login(username='username', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/index.html')

    def test_home_view_deny_anonymous(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login/?next=/')
