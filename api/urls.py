from django.urls import path, include
#from .views import ContactEmail
from . import views

urlpatterns = [
    path('contact/', views.contactemail, name='post'),
    # path('contact/', ContactEmail.as_view(), name='post'),
]