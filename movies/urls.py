from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
from django.urls import path, include

urlpatterns = [
    path('', include('movies.urls')),
]