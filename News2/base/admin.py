from django.contrib import admin
from .models import Topic, News, Comment, User

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(News)
admin.site.register(Comment)