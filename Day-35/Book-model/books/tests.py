# books/tests/test_books_api.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from books.models import Book
import datetime

class TestBooksAPI(APITestCase):
    def setUp(self):
        # Users
        self.user = User.objects.create_user(username="normal", password="normal123")
        self.admin = User.objects.create_user(username="adminuser", password="admin123", is_staff=True)

        # Tokens
        self.token_user = Token.objects.create(user=self.user)
        self.token_admin = Token.objects.create(user=self.admin)

        # Some books
        Book.objects.create(title="Book One", author="Author A", published_date=datetime.date(2020,1,1))
        Book.objects.create(title="Book Two", author="Author B", published_date=datetime.date(2021,6,1))

        self.list_url = reverse("book-list")      # from router
        # token headers:
        self.user_auth = {"HTTP_AUTHORIZATION": f"Token {self.token_user.key}"}
        self.admin_auth = {"HTTP_AUTHORIZATION": f"Token {self.token_admin.key}"}

    def test_get_books_list_and_detail(self):
        # list
        res = self.client.get(self.list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(res.data["results"]), 2)

        # detail
        first = Book.objects.first()
        detail_url = reverse("book-detail", args=[first.pk])
        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["title"], first.title)

    def test_post_unauthenticated_forbidden(self):
        payload = {"title": "New Book", "author": "Author C", "published_date": "2022-01-01"}
        res = self.client.post(self.list_url, payload, format="json")
        # TokenAuthentication + custom permission => unauthenticated => 401 Unauthorized
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_authenticated_success(self):
        payload = {"title": "New Book", "author": "Author C", "published_date": "2022-01-01"}
        res = self.client.post(self.list_url, payload, format="json", **self.user_auth)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.filter(title="New Book").count(), 1)

    def test_put_authenticated_success(self):
        book = Book.objects.create(title="Updatable", author="Author D")
        detail_url = reverse("book-detail", args=[book.pk])
        payload = {"title": "Updated Title", "author": "Author D", "published_date": "2022-05-05"}
        res = self.client.put(detail_url, payload, format="json", **self.user_auth)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Updated Title")

    def test_delete_requires_admin(self):
        book = Book.objects.create(title="ToDelete", author="Author E")
        detail_url = reverse("book-detail", args=[book.pk])

        # unauthenticated -> 401
        res = self.client.delete(detail_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

        # authenticated but not admin -> 403 Forbidden
        res = self.client.delete(detail_url, **self.user_auth)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # admin -> 204 No Content
        res = self.client.delete(detail_url, **self.admin_auth)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
