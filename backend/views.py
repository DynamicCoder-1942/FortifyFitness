from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import joblib
from datetime import datetime
from home.models import Contact
from home.models import Post
from django.contrib import messages



boosting_model = joblib.load('descision_tree.pkl')



def index(request):
    return render(request, 'index.html')

def fitness(request):
    return render(request, 'fitness.html')

def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blog.html', context)    

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'We have RECEIVED you MESSAGE SUCCESSFULLY....!!! ')
    return render(request, 'contact.html')

def bmi(request):
    return render(request, 'bmi.html')

def whr(request):
    return render(request, 'whr.html')

def calories(request):
    return render(request, 'calories.html')

def heart(request):
    return render(request, 'heart.html')

def diabetes(request):


    return render(request,'diabetes.html')



def predictions(request):
    a = request.GET.get('age')
    b = request.GET.get('gender')
    c = request.GET.get('polyuria')
    d = request.GET.get('polydipsia')
    e = request.GET.get('weightloss')
    f = request.GET.get('weakness')
    g = request.GET.get('polyphagia')
    h = request.GET.get('genitalthrush')
    i = request.GET.get('visualblurring')
    j = request.GET.get('itching')
    k = request.GET.get('irritability')
    l = request.GET.get('delayedhealing')
    m = request.GET.get('partialparesis')
    n = request.GET.get('musclestiffness')
    o = request.GET.get('alopesia')
    p = request.GET.get('obesity')
    
    arr = np.array([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]])
    result = boosting_model.predict(arr)
    if result==1:
        s = "THE PATIENT IS DIABETIC AND NEEDS TO CONSULT A DOCTOR"
        
    else:
        s = "THE PATIENT IS HEALTHY AND NON DIABETIC"


    params = {'result': s}


    return render(request,'diabetes_result.html', params)



    

def blog1(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {"post":post}
    return render(request, 'blog1.html', context)
"""
def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def blog4(request):
    return render(request, 'blog4.html')

def blog5(request):
    return render(request, 'blog5.html')

def blog6(request):
    return render(request, 'blog6.html')
    """