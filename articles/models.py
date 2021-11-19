from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    summery = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    image = models.FileField(upload_to="images/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    manba = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
