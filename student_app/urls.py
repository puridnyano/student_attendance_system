from django.contrib import admin
from django.urls import path
from . import views
from . import hodviews,staffviews,studentviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name='login'),
    #HOD URLS
    path('hod_home/',hodviews.hod_home,name='hod_home'),
    #STAFF URLS
    path('staff_home/',staffviews.staff_home,name='staff_home'),
    #STUDENT URLS
    path('student_home/',studentviews.student_home,name='student_home'),
]
