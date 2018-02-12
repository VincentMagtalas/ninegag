from django.conf.urls import url
from django.urls import path
from post import views


urlpatterns = [
    #User Registration
    url(r'^register/', views.register),

    #Posts
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # ex: 5/comment/
    url(r'^(?P<pk>\d+)/comment$', views.post_comment, name='post_comment'),
    url(r'^(?P<pk>\d+)/subcomment$', views.comment_subcomment, name='comment_subcomment'),
    url(r'^(?P<pk>\d+)/votecomment$', views.vote_comment, name='vote_comment'),
    url(r'^(?P<pk>\d+)/votesubcomment$', views.vote_subcomment, name='vote_subcomment'),

]