from django.http import HttpResponse
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/home.html", {"categories": categories, "items": items})

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect("/login/")
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {"form": form})