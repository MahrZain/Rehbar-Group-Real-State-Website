from django.shortcuts import render, redirect
from app.models import Home, About, Service, Feature, ContactInfo, SocialMedia, Contact
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name, email=email, message=message
        )
        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('home')

    context = {
        'home_data': Home.objects.all(),
        'about_data': About.objects.all(),
        'services': Service.objects.all(),
        'projects': Feature.objects.all(),
        'contact_info': ContactInfo.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'index.html', context)
