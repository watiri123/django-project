from django.shortcuts import render

# Create your views here.
import datetime

def christmas(request):
    now = datetime.datetime
    return render(request, 'index.html',{
        "new": now.month == 12 and now.day == 25
    })
