from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def photos(request):
    return render(request, 'photos.html')


