from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return f'author: {self.author}, title: {self.title}'

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.pk)])