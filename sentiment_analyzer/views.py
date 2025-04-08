from django.shortcuts import render
from textblob import TextBlob
from prometheus_client import Histogram, Counter
from .models import Analysis

# Métriques Prometheus
PAGE_LOAD_TIME = Histogram('page_load_seconds', 'Temps de chargement des pages')
FAILED_LOGIN_ATTEMPTS = Counter('failed_login_attempts_total', 'Total failed login attempts')

def analyze_view(request):
    with PAGE_LOAD_TIME.time():
        sentiment = None
        if request.method == 'POST':
            text = request.POST.get('text', '')
            sentiment = TextBlob(text).sentiment.polarity
            Analysis.objects.create(text=text, score=sentiment)
        return render(request, 'index.html', {'sentiment': sentiment})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return render(request, 'index.html', {'message': 'Connexion réussie'})
        else:
            FAILED_LOGIN_ATTEMPTS.inc()
            return render(request, 'login.html', {'error': 'Identifiants invalides'})
    return render(request, 'login.html')
