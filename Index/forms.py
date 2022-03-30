from django.forms import ModelForm

from Index.models import ModelBackForm


class BackForms(ModelForm):
    class Meta:
        model = ModelBackForm
        fields = ['minPrice', 'maxPrice', 'service', 'name', 'email', 'phone', 'file', 'message']
