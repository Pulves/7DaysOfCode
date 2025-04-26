from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.get_characters, name="characters"),
]