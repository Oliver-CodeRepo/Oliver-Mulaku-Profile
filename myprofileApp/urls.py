from django.urls import path

from . import views

urlpatterns = [
    path('oliver_mulaku/home/', views.homePage, name='home'),
    path('oliver_mulaku/home/my-resume/', views.downloadFile, name='resume')
]