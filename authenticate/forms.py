from django import forms
from.models import Signup,Login


class SignupForm(forms.ModelForm):
    
    class Meta:
        model = Signup
        fields = '__all__'
        widgets = {
            'password1':forms.PasswordInput(attrs={'placeholder':'Enter your password','class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'Confirm your password','class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter your firstname','class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter your lastname','class': 'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your Email','class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder':'Enter your username','class': 'form-control'})
        }


        labels = {
            'first_name':'first name',
            'last_name': 'last name',
            'username':'username',
            'email':'email',
            'password1':'password',
            'password2':'password',

        }

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Login
        fields = '__all__'
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'Enter your password','class': 'form-control'}),
            'username':forms.TextInput(attrs={'placeholder':'Enter your username','class': 'form-control'}),
             
        }
        

        labels = {
            'username':'username',
            'password':'password',
        }