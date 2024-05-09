from django import forms
from django.forms import ModelForm, Select
from .models import Georeference, EconomicMain, EconomicSub
from .utils import get_choices

class SearchForm(forms.Form):

    geographic_level = forms.ChoiceField(
        choices=[('City of Chicago', 'City of Chicago'),
                 ('Community Area', 'Community Area'),
                 ('Zipcode', 'Zipcode'),
                 ('Tract', 'Tract')],
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )

    tract = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_choices(Georeference, 'id'))
    
    category = indicator = forms.ChoiceField(
        choices=[('Economic', 'Economic'), 
                 ('Education', 'Education'), ('Health', 'Health'),
                 ('Housing', 'Housing'), ('Population', 'Population')],
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )

    indicator = forms.ChoiceField(
        choices=get_choices(EconomicMain, 'indicator_name'),
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )

    year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_choices(EconomicMain, 'year'))

class SubgroupForm(forms.Form):
    subgroup_year = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    def __init__(self, year_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subgroup_year'].choices = year_choices
# class SearchForm(forms.Form):
#     period = forms.ModelChoiceField(queryset = Georeference.objects.all())
#         #period = forms.ModelChoiceField(queryset = Georeference.objects.all(), widget=forms.CheckboxSelectMultiple)
#         #period = forms.ModelChoiceField(queryset = Georeference.objects.values_list('zip_code', flat=True).distinct().order_by())
#         #period = forms.ModelChoiceField(queryset = EconomicMain.objects.values('year'))

# class SearchForm(ModelForm):
#     class Meta:
#         model = Georeference
#         fields = ['zip_code']
        
#         period = forms.ModelChoiceField(
#             queryset=Georeference.objects.all().values('zip_code').distinct().order_by('zip_code'),
#             to_field_name='zip_code',
#             required=True,  
#             widget=forms.Select(attrs={'class': 'form-control'})
# )

        