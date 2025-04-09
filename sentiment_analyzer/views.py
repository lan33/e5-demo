from django.shortcuts import redirect, render
from textblob import Blobber, TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from prometheus_client import Histogram, Counter
from .models import Analysis

TEXT_BLOB = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

# Métriques Prometheus
PAGE_LOAD_TIME = Histogram('page_load_seconds', 'Temps de chargement des pages')
FAILED_LOGIN_ATTEMPTS = Counter('failed_login_attempts_total', 'Total failed login attempts')

def analyze_view(request):
    with PAGE_LOAD_TIME.time():
        sentiment = None
        if request.method == 'POST':
            text = request.POST.get('text', '')
            blob = TEXT_BLOB(text)
            sentiment = blob.sentiment[0]
            Analysis.objects.create(text=text, score=sentiment)
        return render(request, 'index.html', {'sentiment': sentiment})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('/')
        else:
            FAILED_LOGIN_ATTEMPTS.inc()
            return render(request, 'login.html', {'error': 'Identifiants invalides'})
    return render(request, 'login.html')
