from django.urls import path
from .views import DataView, submit_form 

urlpatterns = [
    path('submit_form', submit_form, name='submit_form'),
    path('data', DataView.as_view(), name='data_view'),
]