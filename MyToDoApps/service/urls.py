from django.urls import path
from . import views 

urlpatterns = [
    path('post-property/', views.post_property, name='post_property'),
    path('propertes',views.user_properties,name='property_list'),
]
