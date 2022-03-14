from django import forms

choices = [
    ('0', 'Not At All'),
    ('1', 'Somewhat'),
    ('2', 'Moderately'),
    ('3', 'A lot'),
    ('4', 'Extremely')
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

    field16 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field17 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field18 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field19 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field20 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)

    field21 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field22 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field23 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field24 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
    field25 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)
