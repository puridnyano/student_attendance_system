from django.shortcuts import render

# Create your views here.
def staff_home(request):
    return render(request, 'staff_template/staff_home.html')