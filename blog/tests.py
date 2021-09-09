from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = Post.objects.create(
            category_id=1, name='Name',  nit='Nit', adress='Direccion', phone='phone', author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        nit = f'{post.nit}'
        name = f'{post.name}'
        adress=f'{post.adress}'
        phone = f'{post.phone}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(name, 'Post Title')
        self.assertEqual(phone, 'Post Content')
        self.assertEqual(adress, 'Post Excerpt')
        self.assertEqual(nit, 'Post Excerpt')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")