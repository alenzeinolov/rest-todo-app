from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Category

User = get_user_model()


class CategoriesTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="test_user1", password="test_user1"
        )
        self.user2 = User.objects.create_user(
            username="test_user2", password="test_user2"
        )

    def test_create_category(self):
        url = reverse("api:category-list")
        data = {"name": "Personal"}

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, "Personal")

    def test_delete_own_category(self):
        category = Category.objects.create(name="To Delete", author=self.user1)
        url = reverse("api:category-detail", args=[str(category.uid)])

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Category.objects.count(), 0)

    def test_delete_category_fail(self):
        category = Category.objects.create(name="Cannot Delete", author=self.user2)
        url = reverse("api:category-detail", args=[str(category.uid)])

        self.client.login(username="test_user1", password="test_user2")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(Category.objects.count(), 1)

    def test_can_see_only_own_categories(self):
        url = reverse("api:category-list")

        Category.objects.create(name="Test User 1", author=self.user1)
        Category.objects.create(name="Test User 2", author=self.user2)

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test User 1")
