from django.urls import path
from Attendence import views
from .views import mark_attendance

urlpatterns = [
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
]
