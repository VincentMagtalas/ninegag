from django.db import models

from post.models import Post

# Create your models here.
class Comment(models.Model):

    comment = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    postid = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('postid','comment','upvote','downvote','created','owner')

class SubComment(models.Model):

    subcomment = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    commentid = models.ForeignKey(Comment, related_name='subcomments', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='subcomments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('commentid','subcomment','upvote','downvote','created','owner')