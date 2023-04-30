# from django.http import HttpResponse
# from django.template import Context, loader

# def index(request):
#     template = loader.get_template("home_page.html")
#     return HttpResponse(template.render())

from django.shortcuts import render

def index(request):
    return render(request, 'home_page.html')

# Create your views here.
