from django import forms
from django.forms import TextInput, Textarea

from basic_info.models import CustomerInfo


class AddCustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = (
            'location', 'name', 'mobilephones',
            'address', 'phone', 'default_rebate',

        )
        widgets = {
            'location': TextInput(attrs={'class': 'form-control info_input'}),
            'name': TextInput(attrs={'class': 'form-control info_input'}),
            'mobilephones': TextInput(attrs={'class': 'form-control info_input'}),
            'address': Textarea(attrs={'class': 'form-control info_area', 'rows': '3', 'cols': '19'}),
            'phone': TextInput(attrs={'class': 'form-control info_input'}),
            'default_rebate': TextInput(attrs={'class': 'form-control info_input'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddCustomerInfoForm, self).__init__(*args, **kwargs)
        self.fields['mobilephones'].required = False
        self.fields['phone'].required = False
        self.fields['address'].required = False
