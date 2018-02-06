from django import forms

from acs.models import Profile


class StudentForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('tuition',)
