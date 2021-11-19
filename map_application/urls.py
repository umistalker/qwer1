from . import views
from django.urls import path



urlpatterns = [
    path('', views.rendermap, name='rendermap'),
    path('post_dot/', views.post_dot, name = 'post_dot'),
    path('get_dot/', views.get_dot, name='get_dot')

]