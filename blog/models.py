from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(default=timezone.now)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Comment(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        created = models.DateField(default=timezone.now)
        content = models.TextField()

        class Meta:
            verbose_name = 'Comment'
            verbose_name_plural = 'Comments'

        def __str__(self):
            return str(self.content)