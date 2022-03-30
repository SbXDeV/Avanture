from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.Index, name='index'),
    path('case/id/<int:pk>/', views.DetailCase, name='case'),

]
