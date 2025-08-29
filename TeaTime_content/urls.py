from django.urls import path

from . import views

app_name = "TeaTime_content"

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    path('bread_and_honey/', views.bread_and_honey, name='bread_and_honey'),
    path('flapjack/', views.flapjack, name='flapjack'),
]
