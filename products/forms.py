from django import forms
from .models import BikeBrand, BikeModel

class BikeFilterForm(forms.Form):
    company = forms.ModelChoiceField(queryset=BikeBrand.objects.none(), required=True)
    model = forms.ModelChoiceField(queryset=BikeModel.objects.none(), required=True)
  
  
  
    def __init__(self, *args, **kwargs):
        super(BikeFilterForm, self).__init__(*args, **kwargs)
        if self.is_bound and 'company' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['model'].queryset = BikeModel.objects.filter(id=company_id)
            except (ValueError, TypeError):
                pass
