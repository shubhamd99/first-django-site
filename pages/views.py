from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {})
    

def about(request):
    from pages.namer import shubham
    return render(request, "about.html", {"my_about": shubham})


def contact(request):
    return render(request, "contact.html", {})

    
