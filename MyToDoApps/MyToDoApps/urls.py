"""
URL configuration for MyToDoApps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MyToDoApps import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('',views.homedetail),
    path('homee/',views.homee),
    path('about/', views.about, name='about'),
    path('test/',views.test),
    path('properties/', views.properties, name='properties'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('form/',views.form_login),
    path('login/',views.login),
    path('error/', views.error, name='error'), 
    path('result/', views.result, name='result'), 
    path('', views.homee, name='home'),  
    path('real/', views.real, name='real'), 
    path("chatbot-ui/", views.chatbot_page, name="chatbot_page"), 
    path("chatbot/", views.chatbot_response, name="chatbot_response"),
    path('ar-home/', views.ar_home_view, name='ar-home'),
    path('', include('service.urls')),
    # path('property-info/', views.property_info, name='property_info')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

