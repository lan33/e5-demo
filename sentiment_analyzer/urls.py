from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.analyze_view, name='analyze'),
    path('metrics/', include('django_prometheus.urls')),
]
