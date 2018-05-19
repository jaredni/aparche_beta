from acs.models import Transaction, Profile
from acs.forms.transaction import TransactionForm

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic


class CreateView(generic.CreateView):
    template_name = 'acs/transaction/create.html'
    model = Transaction
    form_class = TransactionForm

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        student_pk = self.kwargs['student_pk']
        context['STUDENT'] = Profile.objects.get(pk=student_pk)

        return context

    def form_valid(self, form):
        self.object = form.save(False, self.kwargs['student_pk'])
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse(
            'detail-student', args=(self.kwargs['student_pk'], ))
