from django.urls import path
from videogames import views


urlpatterns = [
    path('create/', views.videogame_create, name='videogame_create'),
    path('<slug:slug>/', views.VideogameDetailView.as_view(), name='videogame_view'),
    path('delete/<slug:slug>', views.VideogameDeleteView.as_view(), name='videogame_delete'),
    path('update/<slug:slug>', views.videogame_update, name='videogame_update'),
]