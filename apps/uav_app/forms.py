from django import forms
from .models import Rental, UCAV, User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = [ 'notes', ]
        

        widgets = {
            'notes': forms.Textarea(attrs={
                'class': 'relative w-full !bg-zinc-700 text-white border border-zinc-600 focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50 rounded-md shadow-sm px-3 py-2',
                'rows': 3,

            }),
        }
        error_messages = {
            'start_date': {
                'required': _("Start date is required."),
            },
            'end_date': {
                'required': _("End date is required."),
                'invalid': _("Enter a valid end date."),
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError(_("End date should be after the start date."))

        return cleaned_data
