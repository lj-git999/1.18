from django.urls import path

from apiapp import views

urlpatterns=[
    path('user/',views.UserAPIView.as_view()),
    path('computer/',views.ComputerAPIView.as_view()),
]