from django.contrib import admin
from .models import Board, Post, License, Permission

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(License)
admin.site.register(Permission)
