from django.conf.urls import url

from . import views
from .views import student

urlpatterns = [
    url(r'^student/create/$', student.CreateView.as_view(),
        name='create-student'),
    url(r'^student/list/$', student.ListView.as_view(), name='list-student'),
    url(r'^student/detail/(?P<pk>\d+)$', student.DetailView.as_view(),
        name='detail-student'),
    url(r'^student/delete/(?P<pk>\d+)$', student.DeleteView.as_view(),
        name='delete-student'),
]
