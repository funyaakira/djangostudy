from django.contrib import admin
from .models import Board, Post, License, Permission, Topic

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Topic)


admin.site.register(License)
admin.site.register(Permission)
