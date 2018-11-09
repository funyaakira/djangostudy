from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

from datetime import time
from django.utils.html import mark_safe
from markdown import markdown

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))



#  ------------------------------------------------------------------------------------------- #

GENDER_CHOICES = (
    ("女性", "女性"),
    ("男性", "男性"),
)

TIME_CHOICES = [
    (time(hour,00,00), "{0}時".format(hour)) for hour in range(9,16)
]

class License(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField("名前", max_length=255)
    age = models.IntegerField("年齢", null=True)
    license = models.ManyToManyField(License, verbose_name="資格")
    permission = models.ForeignKey(Permission, verbose_name="えらさ", on_delete=models.CASCADE)
    gender = models.CharField("性別", max_length=2, blank=True, choices=GENDER_CHOICES)
    login = models.TimeField("ログイン可能時間", choices=TIME_CHOICES)

    def __str__(self):
        return self.name
