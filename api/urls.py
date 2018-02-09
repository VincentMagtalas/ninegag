from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/$', views.api_root),
    url(r'^api/post/$', views.GenericPostList.as_view(), name='post-list'),
    url(r'^api/post/(?P<pk>[0-9]+)/$', views.GenericPostDetail.as_view(), name='post-detail'),
    url(r'^api/comment/$', views.GenericCommentList.as_view(), name='comment-list'),
    url(r'^api/comment/(?P<pk>[0-9]+)/$', views.GenericCommentDetail.as_view(), name='comment-detail'),
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api/subcomment/$', views.GenericSubCommentList.as_view(), name='subcomment-list'),
    url(r'^api/subcomment/(?P<pk>[0-9]+)/$', views.GenericSubCommentDetail.as_view(), name='subcomment-detail'),
]