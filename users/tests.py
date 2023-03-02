from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testusertest', email='testusertest@domain.com', password='testpass123')
        self.assertEqual(user.username, "testusertest")
        self.assertEqual(user.email, "testusertest@domain.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)