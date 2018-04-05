from acs.models import Level
from acs.forms.level import LevelForm

from django.core.urlresolvers import reverse_lazy
from django.views import generic


class ListView(generic.ListView):
    template_name = 'acs/level/list.html'
    model = Level


class CreateView(generic.CreateView):
    template_name = 'acs/level/create.html'
    model = Level
    form_class = LevelForm
    success_url = reverse_lazy('list-level')


class DetailView(generic.DetailView):
    template_name = 'acs/level/detail.html'
    model = Level


class DeleteView(generic.DeleteView):
    template_name = 'acs/level/delete.html'
    model = Level
    success_url = reverse_lazy('list-level')
