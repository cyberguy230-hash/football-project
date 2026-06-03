from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Football
from django.contrib.auth.models import User
# Create your views here.
def soccer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        team = request.POST.get("team_name")
        player = request.POST.get("player_name")

        Football.objects.create(
            Name = name,
            Age = age,
            Team = team,
            Player = player
        )

        return redirect("/submit/")
    return render(request, "football.html")

def submit(request):
    if request.method == "POST":
        # handle form data here
        ...
        return render(request, "submit.html")
    else:
        return render(request, "submit.html")
    
def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="superadmin",
            email="admin@test.com",
            password="superadmin@2064"
        )
        return HttpResponse("Admin created")
    return HttpResponse("Already exists")