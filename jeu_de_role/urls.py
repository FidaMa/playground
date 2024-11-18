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
]
