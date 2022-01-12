from django.shortcuts import render
from django.http import HttpResponse
from event.models import *

from django.core.paginator import PageNotAnInteger, Paginator
from django.shortcuts import render,redirect
import math, random
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate, logout
from event.models import *
from TSGhackathon.models import *
import openpyxl
from datetime import date
from django.contrib.auth.models import User as defaultuser
from django.contrib.auth.models import auth

from django.core.paginator import PageNotAnInteger, Paginator
# Create your views here.

def dashboard(request):
    social = Social.objects.all()
    context = {
        'social':social,
    }
    return render(request, 'events/dashboard.html', context)

def dashboard_add_social(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        small_description = request.POST['small_description']
        image = request.POST['image']
        description = request.POST['description']
        month_of_event = request.POST['month_of_event']
        date = request.POST['date']
        type_of_event = request.POST['type_of_event']
        day_of_event = request.POST['day_of_event']
        SuperviserName = request.POST['SuperviserName']
        SuperviserEmail = request.POST['SuperviserEmail']
        SuperviserContact = request.POST['SuperviserContact']
        VenueName = request.POST['VenueName']
        facebook = request.POST['facebook']
        linkedin = request.POST['linkedin']
        instagram = request.POST['instagram']
        print(name)
        social_add = Social(name=name,small_description=small_description,image=image,description=description,month_of_event=month_of_event,
            date=date,type_of_event=type_of_event,day_of_event=day_of_event,SuperviserName=SuperviserName,SuperviserEmail=SuperviserEmail,SuperviserContact
            =SuperviserContact,VenueName=VenueName,facebook=facebook,linkedin=linkedin,instagram=instagram)
        social_add.save()
        return HttpResponse("hello")
    else:    
        social = Social.objects.all()
        context = {
            'social':social,
        }
        return render(request, 'events/dashboard_add_social.html', context)



def interIIT(request):
    context = {
    }
    return render(request, 'results/tables-data.html', context)


def interIITsocult(request):
    context = {
    }
    return render(request, 'results/interIIT-socult.html', context)


def interIITtechnology(request):
    context = {
    }
    return render(request, 'results/inter-IIT-technology.html', context)


def GCTechnology(request):
    context = {
    }
    return render(request, 'results/charts-chartjs.html', context)


def GCSocult(request):
    context = {
    }
    return render(request, 'results/GCsocult.html', context)

def eventhome(request):
    context = {
    }
    return render(request, 'events/base.html', context)

def technology(request):
    technology = Technology.objects.all()
    # context = {
    #     'technology': technology, 
    # }
    p=Paginator(technology, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    P=Profile.objects.get(username=request.user)
    print("USer Successfullyy logged in ")
    print("USername= "+ str(request.user)+"has fullname ="+str(P.fullname) )
    print(P.fullname)
    context={
        'technology': technology,
        'page_obj': page_obj,
        'profile':P,
    }
    return render(request, 'events/technology.html', context)

def technology_details(request, name):
    technology = Technology.objects.get(name=name)
    context = {
        'technology': technology,
    }

    return render(request, 'events/technology_details.html', context)

def social(request):
    social = Social.objects.all()
    # context = {
    #     'social': social,
    # }
    p=Paginator(social, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    P=Profile.objects.get(username=request.user)
    print("USer Successfullyy logged in ")
    print("USername= "+ str(request.user)+"has fullname ="+str(P.fullname) )
    print(P.fullname)
    context={
    'social': social,
    'page_obj': page_obj,
    'profile':P,
    
    }
    return render(request, 'events/SocialCulture.html', context)



def studentWelfare(request):
    studentWelfare = StudentWelfare.objects.all()
    # context = {
    #     'studentWelfare': studentWelfare,
    # }
    p=Paginator(studentWelfare, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    P=Profile.objects.get(username=request.user)
    print("USer Successfullyy logged in ")
    print("USername= "+ str(request.user)+"has fullname ="+str(P.fullname) )
    print(P.fullname)
    context={
    'studentWelfare': studentWelfare,
    'page_obj': page_obj,
    'profile':P,
    }
    return render(request, 'events/studentWelfare.html', context)


def social_details(request, name):
    social = Social.objects.get(name=name)
    context = {
        'social': social,
    }
    return render(request, 'events/social_details.html', context)

def studentWelfare_details(request, name):
    studentWelfare = StudentWelfare.objects.get(name=name)
    context = {
        'studentWelfare': studentWelfare,
    }
    return render(request, 'events/studentWelfare_details.html', context)

def sports(request):
    sports = Sports.objects.all()
    # context = {
    #     'sports': sports,
    # }
    p=Paginator(sports, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    P=Profile.objects.get(username=request.user)
    print("USer Successfullyy logged in ")
    print("USername= "+ str(request.user)+"has fullname ="+str(P.fullname) )
    print(P.fullname)
    context={
    'sports': sports,
    'page_obj': page_obj,
    'profile':P,
    }
    return render(request, 'events/SportsAndGames.html', context)

def sports_details(request, name):
    sports = Sports.objects.get(name=name)
    context = {
        'sports': sports,
    }
    return render(request, 'events/sports_details.html', context)

def result(request):
    context={

    }
    return render(request, 'results/index.html', context)



# def listing(request):
#     studentWelfare = StudentWelfare.objects.all()
#     technologys = Technology.objects.all()
#     socials = Social.objects.all()
#     sports = Sports.objects.all()

#     context = {
#         'studentWelfare': studentWelfare,
#         'technologys':technologys,
#         'socials':socials,
#         'sports':sports,
#     }
#     paginator = Paginator(context, 6) # Show 6 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'technology.html', {'page_obj': page_obj})

