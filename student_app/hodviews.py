from django.shortcuts import render

# Create your views here.
def hod_home(request):
    return render(request, 'hod_template/hod_home.html')