from django.contrib import admin
from .models import Topic, News, Comment

admin.site.register(Topic)
admin.site.register(News)
admin.site.register(Comment)