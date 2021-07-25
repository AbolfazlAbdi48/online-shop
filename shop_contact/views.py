from django.shortcuts import render
from shop_setting.models import Setting
from .forms import CreateContactForm
from .models import ContactUs

# Create your views here.


def contact_us(request):
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name, email, subject, text = contact_form.cleaned_data.get('full_name'), contact_form.cleaned_data.get(
            'email'), contact_form.cleaned_data.get('subject'), contact_form.cleaned_data.get('text')

        ContactUs.objects.create(name=full_name, email=email, subject=subject, text=text)
        contact_form = CreateContactForm()

    site_setting = Setting.objects.first()

    context = {
        'title': 'تماس با ما | فروشگاه ووگا فودز',
        'slider_title': 'تماس با ووگا فودز',
        'slider_text': 'انتقادات و پینشهادات خودرا با ما به اشتراک بگذازید',
        'contact_form': contact_form,
        'setting': site_setting
    }
    return render(request, 'contact/contact_us.html', context)
