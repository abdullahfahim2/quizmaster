from django import forms

class QuizStartForm(forms.Form):
    user_name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })
    )