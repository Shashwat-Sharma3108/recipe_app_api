"""
    Tests for models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models
class ModelTest(TestCase):
    """
        Testing Models
    """

    def test_create_user_with_email_successful(self):

        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['Test2@EXAMPLE.com','Test2@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'testing@123')
            self.assertEqual(user.email, expected)
    
    def test_new_user_without_email_raises_error(self):
        
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123')
        
    def test_create_super_user(self):
        """
            Test for creating Super User
        """

        user = get_user_model().objects.create_superuser(
            'test123@example.com',
            'super123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass'
        )

        recipe = models.Recipe.objects.create(
            user = user,
            title = 'Test Recipe',
            time_minutes = 5,
            price = Decimal('5.50'),
            description = 'Test Recipe Description'
        )

        self.assertEqual(str(recipe), recipe.title)