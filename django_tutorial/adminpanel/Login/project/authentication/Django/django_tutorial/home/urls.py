from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.login,name='login'),

    path('explore/', views.explore,name='explore'),
    path('About/', views.about,name='about'),
    path('Booking/', views.Booking,name='booking'),
    path('Docters/', views.docters,name='docters'),
    path('Contact/', views.contact,name='contact'),
    path('Department/', views.department,name='department'),
]