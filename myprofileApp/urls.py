from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('my-resume/', views.downloadFile, name='resume')
]