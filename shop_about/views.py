from django.shortcuts import render
from shop_about.models import AboutUs

# Create your views here.


def about_us(request):
    about = AboutUs.objects.first()

    context = {
        'title': 'درباره ما | فروشگاه ووگا فودز',
        'slider_title': 'مارا بیشتر بشناسید',
        'slider_text': 'فروشگاه ووگا فودز',
        'about': about
    }
    return render(request, 'about/about_us.html', context)
