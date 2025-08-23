# books/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
import time

class BookAPIVersioningThrottlingTests(APITestCase):
    def setUp(self):
        # Create user and authenticate
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.client = APIClient()
        self.client.login(username="tester", password="pass123")

        self.book_data = {"title": "Test Book", "author": "Tester", "published_date": "2024-01-01"}

    # ---------------------------
    # VERSIONING TESTS
    # ---------------------------
    def test_url_path_versioning(self):
        url = "/api/v1/books/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_parameter_versioning(self):
        url = "/api/books/?version=1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_header_versioning(self):
        url = "/api/books/"
        response = self.client.get(url, HTTP_X_API_VERSION="1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---------------------------
    # CRUD TEST (POST in v1)
    # ---------------------------
    def test_create_book_v1(self):
        url = "/api/v1/books/"
        response = self.client.post(url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ---------------------------
    # THROTTLING TESTS
    # ---------------------------
    def test_throttling_exceeded(self):
        url = "/api/v1/books/"
        # Make 5 requests (limit is 5 per minute from settings)
        for _ in range(5):
            self.client.get(url)

        # 6th request should be throttled
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_throttling_resets_after_time(self):
        url = "/api/v1/books/"
        for _ in range(5):
            self.client.get(url)

        # Wait for throttle reset (60s window from settings)
        time.sleep(61)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
