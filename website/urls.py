from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('blog-single.html', views.Blog, name='Blog'),
    path('portfolio-details.html', views.details, name='details'),
    path('news-single.html', views.news, name='news'),
    path('services.html', views.services, name='services'), 
    path('ambulance.html', views.ambulance, name='ambulance'), 
    path('appointment.html', views.appointment, name='appointment'), 
    path('404.html', views.Error_404, name='Error_404'),



]
