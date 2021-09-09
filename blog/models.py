from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
from django.conf import settings
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    options = (
        ('draft','Draft'),
        ('published','Published')
    )
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1,null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    nit = models.TextField(null=True, blank=True)
    phone = models.SlugField(max_length=250, unique_for_date='published',null=True, blank=True)
    published = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts',null=True, blank=True)
    status= models.CharField(max_length=10, choices= options, default='published',null=True, blank=True)
    objects  = models.Manager()
    postobjects=PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


