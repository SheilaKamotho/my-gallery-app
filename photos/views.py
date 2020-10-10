from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def photos(request):
    photos=Image.save_image()
    return render(request, 'photos.html',{"photos":photos})

# def location(request,location_id):
#     try:
#         get_location_id=location.objects.get(pk=location_id)
#         location=image.filter_by_location(get_location_id)
#         message=f'{get_location_id}'
#         return render(request,'location.html',{"message":message,"location":location})
#     except Image.DoesNotExist:
#         Http404('Image does not exist')
    
#     return render(request, 'location.html',{"message":message,"location":location})

        
    
    

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
