from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_user_1 = get_user_model().objects.create_user(username='testuser1', password='passmeup123')
        test_user_1.save()

        test_post = Post.objects.create(title='Test title', body='Test body', author=test_user_1)
        test_post.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_body, 'Test body')
        self.assertEqual(expected_title, 'Test title')
