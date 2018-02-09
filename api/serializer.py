from rest_framework import serializers
from django.contrib.auth.models import User

from post.models import Post
from comment.models import Comment,SubComment

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', format='html')
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('url','id','title', 'code','owner','created','comments')

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail', format='html')
    subcomments = serializers.HyperlinkedRelatedField(many=True, view_name='subcomment-detail', read_only=True)

    class Meta:
        model = Comment
        fields = ('url','comment','upvote','downvote','created','owner','subcomments')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
    subcomments = serializers.HyperlinkedRelatedField(many=True, view_name='subcomment-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts','comments','subcomments')

class SubCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='subcomment-detail', format='html')

    class Meta:
        model = SubComment
        fields = ('url','subcomment','upvote','downvote','created','owner')