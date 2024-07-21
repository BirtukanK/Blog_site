from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('blog-home')
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
    
    def test_home_view(self):
        """Test GET request to home view"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertContains(response, self.post.title)

class PostListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('blog-home')
        self.user = User.objects.create_user(username='Newuser345', password='testing321')
        self.post = Post.objects.create(title='Newusers post updated', content='This is testing post updated', author=self.user)
    
    def test_post_list_view(self):
        """Test GET request to post list view"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertContains(response, self.post.title)

class UserPostListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='Newuser345', password='testing321')
        self.post = Post.objects.create(title='Newusers post updated', content='This is testing post updated', author=self.user)
        self.url = reverse('user-posts', kwargs={'username': self.user.username})
    
    def test_user_post_list_view(self):
        """Test GET request to user post list view"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/user_posts.html')
        self.assertContains(response, self.post.title)