from django.db import models
from django.conf import settings

# Create your models here.

from django.db import models
from django.conf import settings
from datetime import datetime




class Articles(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) 
    tittle = models.CharField(max_length=100)
    article = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='image/',blank=True, null=True)
    post_time = models.DateTimeField(default=datetime.now) 
    def __str__(self):
        return self.tittle
    def snippet(self):
        return self.article[:30]+'....'

 


class login(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'login'

class Register(models.Model):

    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'register'

class Register_Author(models.Model):

    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'register_author'


class Article_Comment(models.Model):

    tittle = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    article_comment =models.CharField(max_length=100)
    comment_time = models.DateTimeField(default=datetime.now)
    approved_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.tittle

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    class Meta:
        db_table = 'article_comment'
