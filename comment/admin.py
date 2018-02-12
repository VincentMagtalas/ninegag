from django.contrib import admin

from .models import Comment,SubComment,Vote

admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Vote)