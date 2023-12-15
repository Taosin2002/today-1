from django import forms 
import datetime
subject = [
    ('math', 'Math'),
    ('english', 'English'),
    ('bangla', 'Bangla'),
]


class ContactForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
    name = forms.CharField(label="Please enter your Name", max_length=100)
    university_name = forms.CharField()
    email = forms.EmailField(required=True)
    roll = forms.IntegerField(initial=0)
    comment = forms.CharField(widget=forms.Textarea)
    value = forms.DecimalField(initial=0.0)  # Replace 0.0 with your default value
    date = forms.DateField()
    birth_date = forms.DateField(input_formats=['%Y-%m-%d'])
    favorite_color = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=subject)
    uplode = forms.FileField()
    img = forms.ImageField()
    agree = forms.BooleanField()


