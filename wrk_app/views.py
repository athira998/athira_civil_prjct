from django.shortcuts import render,redirect


# Create your views here.

def homepage(request):
    return render(request,'home.html')




def wrk(request):
    return render(request,'wrk_updates.html')