from django.shortcuts import render
from .models import OnePage

def home(request):
    sections = OnePage.objects.order_by('order').filter(active=True)

    return render(request, 'home/index.html', {'sections': sections})
