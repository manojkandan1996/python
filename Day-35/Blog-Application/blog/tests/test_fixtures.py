from django.core.management import call_command
from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class FixtureLoadTest(TestCase):
    fixtures = ["initial_data.json"]  # Django auto-loads from app/fixtures/

    def test_fixture_loaded(self):
        # Users loaded
        self.assertTrue(User.objects.filter(username="fixture_user").exists())

        # Posts loaded
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, "Fixture Post")
        self.assertEqual(post.author.username, "fixture_user")
