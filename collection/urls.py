from django.urls import path, include
from videogames import views

urlpatterns = [
    path('', views.VideogameListView.as_view(), name='collection'),
    path('videogame/', include('videogames.urls')),
]