from django.shortcuts import render
from .models import Photography


def photography(request):
	photos = Photography.objects
	return render(request, 'photography/photography.html', {'photos': photos}) 