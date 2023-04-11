from django.shortcuts import render

# Create your views here.
def static(request):
    return render(request, 'staticapp.html')
