from django.urls import path, include
from . import views
urlpatterns = [

    path('explore/', views.explore,name='explore'),
    path('About/', views.about,name='about'),
    path('Booking/', views.Booking,name='booking'),
    path('Docters/', views.docters,name='docters'),
    path('Contact/', views.contact,name='contact'),
    path('Department/', views.department,name='department'),
]