from django.shortcuts import render

# Create your views here.

#creating views for home page route
def home(request):
    return render(request, '')  

#views for marketplace page
def marketplace(request):
    return render(request,'')   #html template address in '' as arguement to render method