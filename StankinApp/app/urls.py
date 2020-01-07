from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reg_page/', views.reg, name='reg'),
    path('diary_page/', views.diary, name='diary'),
]
