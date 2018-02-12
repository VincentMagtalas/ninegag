from django.http import HttpResponse
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly
from post.models import Post
from comment.models import Comment,SubComment,Vote
from .serializer import PostSerializer,CommentSerializer,UserSerializer,SubCommentSerializer,VoteSerializer
from .serializer import  XSubCommentSerializer, XCommentSerializer,XPostSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('posts-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format),
        'subcomments': reverse('subcomment-list', request=request, format=format),

        'xpost': reverse('xpost-list', request=request, format=format),
        'xcomments': reverse('xcomment-list', request=request, format=format),
        'xsubcomments': reverse('xsubcomment-list', request=request, format=format),

    })

class GenericPostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GenericPostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class GenericCommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GenericCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GenericSubCommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GenericSubCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer

class GenericVoteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GenericVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
#===================================================================================

class XSubCommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = SubComment.objects.all()
    serializer_class = XSubCommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class XCommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Comment.objects.all()
    serializer_class = XCommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class XPostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = XPostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class XPostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = XPostSerializer