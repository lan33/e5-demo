from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_view, name='analyze'),
    path('login/', views.login_view, name='login')
]
