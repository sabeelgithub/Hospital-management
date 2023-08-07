
from django import forms
from.models import Booking 
class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'p_name':forms.PasswordInput(attrs={'placeholder':'Enter your name','class': 'form-control'}),
            'p_phone':forms.PasswordInput(attrs={'placeholder':'Enter your no','class': 'form-control'}),
            'p_email':forms.TextInput(attrs={'placeholder':'Enter your email','class': 'form-control'}),
            'doc_name':forms.Select(attrs={'placeholder':'choose your docter','class': 'form-control'}),
            'booking_date':DateInput(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'p_name':'Patient Name: ',
            'p_phone':'Patient Phone: ',
            'p_email':'Patient Email: ', 
            'doc_name':'Docter Name: ',
            'booking_date':'Booking Date: ', 
            


        }
