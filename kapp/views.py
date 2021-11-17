
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import UserInfo


def login(request):
    return render(request, "kapp/login.html")


def login_handler(request):
    if request.method == "POST":
        uemormob = request.POST.get("emormob")
        upass = request.POST.get("password")

        user = UserInfo.objects.get(emormob=uemormob)

        if upass == user.password:
            return HttpResponseRedirect(reverse("kapp:home", args=(user.user_name,)))


def home(request, user_id):
    return render(request, "kapp/home.html", {"user_name": user_id})


def registration(request):
    return render(request, "kapp/registration.html")


def registration_handler(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        uemormob = request.POST.get("emormob")
        upass = request.POST.get("password")

        user = UserInfo(user_name=uname, emormob=uemormob, password=upass)
        user.save()

        return HttpResponseRedirect(reverse("kapp:login"))
