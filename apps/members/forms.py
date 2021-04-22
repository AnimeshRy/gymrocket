from django import forms
from .models import Member


class AddMemberForm(forms.ModelForm):
    # Add new Member form
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['registration_upto']

        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'medical_history': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }

    def clean_mobile_number(self, *args, **kwargs):
        # Check for mobile number and return Validation Error if incorrect
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit():
            raise forms.ValidationError('Mobile number should be a number')
        if Member.objects.filter(mobile_number=mobile_number).exists():
            raise forms.ValidationError(
                'This mobile number has already been registered.')
        else:
            if len(str(mobile_number)) == 10:
                return mobile_number
            else:
                raise forms.ValidationError(
                    'Mobile number should be 10 digits long.')
        return mobile_number

    def clean_amount(self):
        # Clean money amount
        amount = self.cleaned_data.get('amount')
        if not amount.isdigit():
            raise forms.ValidationError('Amount should be a number')
        return amount

    def clean(self):
        # Check for already existing member
        cleaned_data = super().clean()
        dob = cleaned_data.get('dob')
        first_name = cleaned_data.get('first_name').capitalize()
        last_name = cleaned_data.get('last_name').capitalize()
        queryset = Member.objects.filter(
            first_name=first_name,
            last_name=last_name,
            dob=dob
        ).count()
        if queryset > 0:
            raise forms.ValidationError('This member already exists!')


class AddMemberUpdateForm(forms.ModelForm):
    # Update Member form without registration_upto date
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['registration_upto']

        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'medical_history': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }
