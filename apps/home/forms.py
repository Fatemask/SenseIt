from django import forms

choices = [
    ('0', 'Not At All'),
    ('1', 'Somewhat'),
    ('2', 'Moderately'),
    ('3', 'A lot'),
    ('4', 'Extremely')
]

category = ['Thoughts and Feelings', 'Activities and Personal Relationships', 'Physical Symptoms', 'Sucidal Urges']

class QuestionnaireForm(forms.Form):
    field1 = forms.ChoiceField(widget=forms.RadioSelect, choices = choices)