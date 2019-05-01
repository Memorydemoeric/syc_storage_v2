from django import forms
from django.forms import widgets
from django.forms import fields


class SearchLocationOrNameForm(forms.Form):
    search_condition = forms.CharField(
        required=False,
        strip=True,
        label='查询',
        initial='',
        widget=widgets.TextInput(attrs={
            'class': "form-control search_condition",
            'placeholder': "地区/客户姓名",
            'id': 'search_condition',
        })
    )


class UploadFileForm(forms.Form):
    upload_file = forms.FileField(
        label='',
        widget=widgets.FileInput(attrs={
            'style': 'display:none',
            'id': 'upload_file',
            'accept': '.xls,.xlsx'
        })
    )
