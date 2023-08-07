from django.contrib import admin
from .models import Departments, Docters,Booking,Login
# Register your models here.
admin.site.register(Departments)
admin.site.register(Docters)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(Login,LoginAdmin)