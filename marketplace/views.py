from django.shortcuts import render

# Create your views here.


#views for marketplace page
def marketplace(request):
    return render(request,'mkplace/market.html')   #html template address in '' as arguement to render method