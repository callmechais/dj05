from django.shortcuts import render

# Create your views here.
def radish(request):
    info = {"key": "mongolia"}
    return render(request, 'pumpkin.html', info)
