from django import forms

from acs.models import Level


class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = "__all__"
