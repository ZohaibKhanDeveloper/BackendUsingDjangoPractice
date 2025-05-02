from django import forms
from django.forms.widgets import NumberInput
FAVORITE_DISH = [
    ('italian','Italian'),
    ('greek','Greek'),
    ('turkish','Turkish'),
]
class NameForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=100)
    age = forms.IntegerField(help_text="Enter a valid age")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    email = forms.EmailField(label='Enter your Email')
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    fav_dish = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_DISH)