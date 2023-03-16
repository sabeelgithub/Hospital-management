from django import forms
from.models import Booking,Login
class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput(),
        }
        labels = {
            'p_name':'Patient Name: ',
            'p_phone':'Patient Phone: ',
            'p_email':'Patient Email: ', 
            'doc_name':'Docter Name: ',
            'booking_date':'Booking Date: ', 
            


        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'

        labels = {
            'username':'username',
            'password':'password',
        }

