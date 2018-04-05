from django import forms

from acs.models import Profile


class StudentForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
