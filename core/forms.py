from django import forms
from core.models import Notes

class Form_for_notes(forms.ModelForm):
    description = forms.CharField(label="Описание",widget = forms.Textarea(attrs={'class': 'form-input','placeholder':'Напишите заметку'}))
    image = forms.FileInput()

    class Meta:
        model = Notes
        fields = ('description','image')

