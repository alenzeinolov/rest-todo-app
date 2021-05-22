from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from ..models import Task

User = get_user_model()


class TasksTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="test_user1", password="test_user1"
        )
        self.category1 = Category.objects.create(name="Personal", author=self.user1)
        self.user2 = User.objects.create_user(
            username="test_user2", password="test_user2"
        )
        self.category2 = Category.objects.create(name="Work", author=self.user2)

    def test_create_task(self):
        url = reverse("api:task-list")
        data = {
            "name": "Buy milk",
            "description": "Test Description",
            "category": self.category1.uid,
            "date": timezone.now().isoformat(),
        }

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().name, data["name"])
        self.assertEqual(Task.objects.first().author.pk, self.user1.pk)
        self.assertFalse(Task.objects.first().is_completed)

    def test_complete_own_task(self):
        task = Task.objects.create(
            name="Buy milk",
            author=self.user1,
            category=self.category1,
            date=timezone.now(),
        )
        url = reverse("api:task-detail", args=[str(task.uid)])
        data = {
            "is_completed": True,
        }

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.patch(url, data, format="json")
        task.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(task.is_completed)

    def test_delete_own_task(self):
        task = Task.objects.create(
            name="Buy milk",
            author=self.user1,
            category=self.category1,
            date=timezone.now(),
        )
        url = reverse("api:task-detail", args=[str(task.uid)])

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Task.DoesNotExist, task.refresh_from_db)

    def test_view_task_fail(self):
        task = Task.objects.create(
            name="Buy milk",
            author=self.user2,
            category=self.category2,
            date=timezone.now(),
        )
        url = reverse("api:task-detail", args=[str(task.uid)])

        self.client.login(username="test_user1", password="test_user1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
