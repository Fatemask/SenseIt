from django import forms

choices = [
    ('0', 'Not At All'),
    ('1', 'Somewhat'),
    ('2', 'Moderately'),
    ('3', 'A lot'),
]

class QuestionnaireForm(forms.Form):
    field1 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field2 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field3 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field4 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field5 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)

    field6 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field7 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field8 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field9 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field10 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)

    field11 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field12 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field13 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field14 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field15 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
