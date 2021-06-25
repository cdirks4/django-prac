from django.urls import path
from . import views


urlpatterns = [
    path('songs/', views.SongList.as_view(), name='songs'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='songs')

]
