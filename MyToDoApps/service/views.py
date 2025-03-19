from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Property

def post_property(request):
    if request.method == 'POST':
        property_data = Property.objects.create(  
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            property_type=request.POST.get('property_type'),
            furnishing=request.POST.get('furnishing'),
            availability=request.POST.get('availability'),
            price=request.POST.get('price'),
            area=request.POST.get('area'),
            images=request.FILES.get('images'),
            contact_name=request.POST.get('contact_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
        )

      
        send_mail(
            subject='Property Submission Confirmation',
            message=f"Hello {property_data.contact_name},\n\nYour property titled '{property_data.title}' has been successfully posted on HomeFinder.\n\nThank you!",
            from_email=settings.BASE_EMAIL,
            recipient_list=[property_data.email],
            fail_silently=False,
        )

        return redirect('post_property')

    return render(request, 'prop.html')
