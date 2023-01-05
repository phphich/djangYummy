from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def history(request):
    return render(request, 'history.html')
def education(request):
    return render(request, 'education.html')
