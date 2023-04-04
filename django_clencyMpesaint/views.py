from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render



cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def pay(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'Clency'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'payments.html')



def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def edit(request):
    return render(request, "edit.html")

def home_page(request):
    return render(request, "home.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        country = request.POST.get('country')
        city = request.POST.get('city')
        amount = request.POST.get('amount')
        gender = request.POST.get('gender')


        query = Student(name=name, email=email, age=age, country=country, city=city, amount=amount, gender=gender)
        query.save()
        return redirect("/")

        return render(request, 'index.html')



def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        country = request.POST.get('country')
        city = request.POST.get('city')
        amount = request.POST.get('amount')
        gender = request.POST.get('gender')


        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.country = country
        update_info.city = city
        update_info.amount = amount
        update_info.gender = gender


        update_info.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
