from django import forms
from .models import Trip
from django.utils import timezone
from django.core.exceptions import ValidationError


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'departure_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'return_date':forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'number_of_travelers': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cd = self.cleaned_data
        if cd['departure_date'] < timezone.now().date() or cd['return_date'] < cd['departure_date']:
            raise ValidationError('Enter a valid date!')
        return super().clean()

