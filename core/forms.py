from django import forms
from core.models import Notes

class Form_for_notes(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('description','image')