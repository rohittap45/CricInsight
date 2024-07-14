from django.shortcuts import render

def index(request):
    return render(request,'CAD/live_matches.html')