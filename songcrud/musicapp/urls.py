"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from musicapp import views

urlpatterns = [
    path('musicapp/', views.artiste_list_and_song_list.as_view()),
    path('musicapp/<int:pk>/', views.songdetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
"""