from django.conf.urls import url
from post import views

urlpatterns = [
    url('post/', views.hello_world),
]