from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email):
            raise forms.ValidationError('このメールアドレスは登録されています。')
