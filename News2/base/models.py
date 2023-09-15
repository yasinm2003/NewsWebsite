from django.db import models
from django.contrib.auth.models import AbstractUser

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    favorite = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class News(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    picture = models.ImageField(default="pexels-alex-andrews-1983037.jpg")
    like = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()