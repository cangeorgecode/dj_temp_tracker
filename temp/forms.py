from .models import Temperature
from django.forms import ModelForm
from django import forms

class TempForm(ModelForm):
    class Meta:
        model = Temperature
        fields = ('temperature', 'smiley', 'remarks')

    def __init__(self, *args, **kwargs):
        super(TempForm, self).__init__(*args, **kwargs)

        self.fields['temperature'].label = ''
        self.fields['temperature'].widget.attrs['class'] = 'form-control'
        self.fields['temperature'].widget.attrs['placeholder'] = 'Temperature'

        self.fields['remarks'].label = ''
        self.fields['remarks'].widget.attrs['class'] = 'form-control'
        self.fields['remarks'].widget.attrs['placeholder'] = 'Remarks'