from django import forms
from .models import MSE_CUSTOMERS
class createForm(forms.ModelForm):
    class Meta:
        model = MSE_CUSTOMERS
        fields = [
            'customer_name',
            'customer_mobile_number',
            'customer_due_amount',
        ]