from django.conf.urls import url

from . import views
from .views import student

urlpatterns = [
    url(r'^create/$', student.CreateView.as_view(), name='create-student'),
    url(r'^student/list/$', student.ListView.as_view(), name='list-student'),
]
