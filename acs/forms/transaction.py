from django import forms

from acs.models import Transaction, Profile


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('amount',)

    def save(self, commit=True, student_pk=0):
        transaction = super(TransactionForm, self).save(commit=False)
        print '*' * 20
        print student_pk
        transaction.student = Profile.objects.get(pk=student_pk)
        transaction.save()
