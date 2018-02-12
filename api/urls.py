from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/$', views.api_root),
    url(r'^api/posts/$', views.GenericPostList.as_view(), name='posts-list'),
    url(r'^api/posts/(?P<pk>[0-9]+)/$', views.GenericPostDetail.as_view(), name='posts-detail'),
    url(r'^api/comment/$', views.GenericCommentList.as_view(), name='comment-list'),
    url(r'^api/comment/(?P<pk>[0-9]+)/$', views.GenericCommentDetail.as_view(), name='comment-detail'),
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api/subcomment/$', views.GenericSubCommentList.as_view(), name='subcomment-list'),
    url(r'^api/subcomment/(?P<pk>[0-9]+)/$', views.GenericSubCommentDetail.as_view(), name='subcomment-detail'),
    url(r'^api/vote/$', views.GenericVoteList.as_view(), name='vote-list'),
    url(r'^api/vote/(?P<pk>[0-9]+)/$', views.GenericVoteDetail.as_view(), name='vote-detail'),

    url(r'^api/xsubcomment/$', views.XSubCommentList.as_view(), name='xsubcomment-list'),
    url(r'^api/xcomment/$', views.XCommentList.as_view(), name='xcomment-list'),
    url(r'^api/xpost/$', views.XPostList.as_view(), name='xpost-list'),
    url(r'^api/xpost/(?P<pk>[0-9]+)/$', views.XPostDetail.as_view(), name='xpost-detail'),
]