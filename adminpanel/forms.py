from django import forms
from.models import AdminLogin
from authenticate.models import Signup
class AdminLoginForm(forms.ModelForm):
    
    class Meta:
        model = AdminLogin
        fields = '__all__'
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'Enter your password','class': 'form-control'}),
            'username':forms.TextInput(attrs={'placeholder':'Enter your username','class': 'form-control'})
            
        }

        labels = {
            'username':'username',
            'password':'password',
        }
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['first_name','last_name','username','email']
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        labels ={
            'first_name':'first name',
            'last_name': 'last name',
            'username':'username',
            'email':'email',
        }       