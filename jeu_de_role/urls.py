from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('lieu/<str:pk>/', views.lieu_detail, name='lieu_detail'),
    path('lieux/', views.lieu_list, name='lieu_list'),
    
    path('character/<str:id_character>/', views.character_detail, name='character_detail'),
    path('character/<str:id_character>/?<str:message>', views.character_detail, name='character_detail_mes'),

    path('characters/', views.character_list, name='character_list'),
    
    path('explore/', views.explore, name='explore'),

    path('add/', views.add_character, name='add_character'),
    path('delete-character/<str:character_id>/', views.delete_character, name='delete_character'),

    path('add_lieu/', views.add_lieu, name='add_lieu'),
    path('delete-lieu/<str:lieu_id>/', views.delete_lieu, name='delete_lieu'),


]

