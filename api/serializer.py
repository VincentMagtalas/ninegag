from rest_framework import serializers
from django.contrib.auth.models import User

from post.models import Post
from comment.models import Comment,SubComment,Vote

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='posts-detail', format='html')
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('url','id','title', 'content','owner','created','comments')

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail', format='html')
    subcomments = serializers.HyperlinkedRelatedField(many=True, view_name='subcomment-detail', read_only=True)

    class Meta:
        model = Comment
        fields = ('url','id','comment','upvote','downvote','created','owner','subcomments')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='posts-detail', read_only=True)
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
        fields = ('url','id','subcomment','upvote','downvote','created','owner')

class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='vote-detail', format='html')
    commentid = serializers.HyperlinkedIdentityField(view_name='comment-detail', format='html',allow_null=True)
    subcommentid = serializers.HyperlinkedIdentityField(view_name='subcomment-detail', format='html',allow_null=True)

    class Meta:
        model = Vote
        fields = ('url','id','owner','reactionid','commentid','subcommentid')

#=======================================================================================================================


class XSubCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    commentid = serializers.HyperlinkedIdentityField(view_name='comment-detail', format='html', allow_null=True)

    class Meta:
        model = SubComment
        fields = ('commentid','id', 'subcomment', 'upvote','downvote','created','owner')

class XCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    subcomments = XSubCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('postid','id', 'comment', 'upvote','downvote','created','owner', 'subcomments')

class XPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='xpost-detail', format='html')
    comments = XCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('url','id', 'title', 'content','owner','created', 'comments')
