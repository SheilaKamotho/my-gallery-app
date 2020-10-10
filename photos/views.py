from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def photos(request):
    photos=Image.save_image()
    return render(request, 'photos.html',{"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
