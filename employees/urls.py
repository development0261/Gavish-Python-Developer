from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', employees,name="employees"),
    path('<int:id>/', getEmplpyee,name="getEmplpyee"),
    path('getAvailableSlots/<int:id>/<int:id2>', getAvailableSlots,name="getAvailableSlots"),
    path('bookAppointment/', bookAppointment,name="bookAppointment"),
]
