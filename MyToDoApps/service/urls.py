from django.urls import path
from . import views 

urlpatterns = [
    path('post-property/', views.post_property, name='post_property'),
]
