from acs.models import Profile
from acs.forms.student import StudentForm

from django.core.urlresolvers import reverse_lazy
from django.views import generic


class ListView(generic.ListView):
    template_name = 'acs/student/list.html'
    model = Profile


class CreateView(generic.CreateView):
    template_name = 'acs/student/create.html'
    model = Profile
    form_class = StudentForm
    success_url = reverse_lazy('list-student')


class DetailView(generic.DetailView):
    template_name = 'acs/student/detail.html'
    model = Profile


class DeleteView(generic.DeleteView):
    template_name = 'acs/student/delete.html'
    model = Profile
    success_url = reverse_lazy('list-student')
