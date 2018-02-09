from django.conf.urls import url
from comment import views

urlpatterns = [
    url('comment/', views.hello_world),
]