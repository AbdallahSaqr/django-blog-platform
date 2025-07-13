from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Tag, Post, ForbiddenWord, Comment, Profile

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(ForbiddenWord)
admin.site.register(Comment)
admin.site.register(Profile)
