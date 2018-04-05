from django.conf.urls import url

from .views import student, level

urlpatterns = [
    # ------------ Students
    url(r'^student/create/$', student.CreateView.as_view(),
        name='create-student'),

    url(r'^student/list/$', student.ListView.as_view(), name='list-student'),

    url(r'^student/detail/(?P<pk>\d+)$', student.DetailView.as_view(),
        name='detail-student'),

    url(r'^student/delete/(?P<pk>\d+)$', student.DeleteView.as_view(),
        name='delete-student'),

    # ------------ Levels
    url(r'^level/create/$', level.CreateView.as_view(),
        name='create-level'),

    url(r'^level/list/$', level.ListView.as_view(),
        name='list-level'),

    url(r'^level/detail/(?P<pk>\d+)$', level.DetailView.as_view(),
        name='detail-level'),

    url(r'^level/delete/(?P<pk>\d+)$', level.DeleteView.as_view(),
        name='delete-level'),
]
