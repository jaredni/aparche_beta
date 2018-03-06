from acs.models import Profile
from acs.forms.student import StudentForm

from django.core.urlresolvers import reverse_lazy
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'acs/index.html'


class ListView(generic.ListView):
    template_name = 'acs/student/list.html'
    model = Profile


class CreateView(generic.CreateView):
    template_name = 'acs/student/create.html'
    model = Profile
    form_class = StudentForm
    success_url = reverse_lazy('create-student')

class DetailView(generic.DetailView):
    template_name = 'acs/student/detail.html'
    model = Profile
