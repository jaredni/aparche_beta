from acs.models import Profile

from django.views import generic


class CreateView(generic.CreateView):
    template_name = 'acs/student/create.html'
    model = Profile
    