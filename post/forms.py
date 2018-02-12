from django import forms

from .models import Post
from comment.models import Comment,SubComment,Vote

class PostForm(forms.ModelForm):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ('title', 'content')

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class CommentForm(forms.ModelForm,):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('postid','comment',)

class SubCommentForm(forms.ModelForm,):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = SubComment
        fields = ('commentid','subcomment',)

class VoteForm(forms.ModelForm,):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Vote
        fields = ('commentid','subcommentid',)