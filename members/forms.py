from gymrocket.settings import DATE_INPUT_FORMATS
from django import forms
from django.forms import fields, widgets
from .models import Member


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['registration_upto']

        widgets = {
            'registration_date': forms.DateInput(format=DATE_INPUT_FORMATS, attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'medical_history': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }
