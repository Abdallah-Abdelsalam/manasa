from django.shortcuts import render, redirect
from django.db.models import Sum
#from django.contrib.auth import authenticate, login, logout
from app.models import Categories,Course,Video

def BASE(request):
    return render(request, "base.html")

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    context ={
        'category':category,
        'course':course,
    }
    return render(request, "main/home.html",context)


def BOOK(request):
    category = Categories.objects.all().order_by('id')[0:5]

    context ={
        'category':category,
        }
    return render(request, "book/book.html",context)


def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)
    course = Course.objects.all()
    context = {
        'category':category,
        'course':course,
    }
    return render(request, "main/single_course.html",context)

def CONTACT_US(request):
    category = Categories.get_all_category(Categories)[0:5]

    context = {
        'category':category,
    }
    return render(request, "main/contact_us.html",context)

def ABOUT_US(request):
    category = Categories.get_all_category(Categories)[0:5]

    context = {
        'category':category,
    }
    return render(request, "main/about_us.html", context)

def PACKAGES(request):
    category = Categories.get_all_category(Categories)[0:5]
    context = {
        'category':category,
    }
    return render(request, "main/packages.html", context)

def SEARCH_COURSE(request):
    category = Categories.get_all_category(Categories)

    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)

    context = {
        'course':course,
        'category':category,
    }

    return render(request, "search/search.html", context)


def COURSE_DETAILS(request,slug):
    category = Categories.get_all_category(Categories)[0:5]
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum=Sum('time_duration'))

    course = Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    
    context = {
        'course':course,
        'category':category,
        'time_duration':time_duration,
        }
    return render(request,'course/course_details.html',context)


def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)[0:5]
    context = {
        'category':category,
        }
    return render(request, "error/404.html",context)


        