from django.urls import path
from students import views

app_name="students"

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.aboutus,name="about"),
    path('contact_us/', views.contact_us,name="contactus"),
]
