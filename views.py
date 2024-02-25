from django.shortcuts import render
from django.http import HttpResponse
tax_rate = 0.15
def index(request):
    return HttpResponse("This is a site to calculate the tax")


def calculate_total(request, price):
    total = price + (price * tax_rate)
    return HttpResponse(f"The total price including tax is: {total}")


def flexable(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def index4(request):
    return HttpResponse(f"the tax rate is {tax_rate*100}%")

def greet(request, name):
    return render(request, "Lab424/greet.html", {
        "name": name.capitalize()
    })