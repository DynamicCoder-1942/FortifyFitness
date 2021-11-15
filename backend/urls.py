"""backend URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('fitness',views.fitness, name='fitness'),
    path('blog',views.blog, name='blog'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('predictions',views.predictions, name='predictions'),
    path('bmi',views.bmi, name='bmi'),
    path('whr',views.whr, name='whr'),
    path('calories',views.calories, name='calories'),
    path('heart',views.heart, name='heart'),
    path('diabetes',views.diabetes, name='diabetes'),
    path('<str:slug>', views.blog1, name='blog1'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)