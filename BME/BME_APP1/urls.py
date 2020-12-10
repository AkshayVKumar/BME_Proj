from django.urls import path
from BME_APP1 import views

app_name="bme_app1"

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.aboutus,name="about"),
    path('contact_us/', views.contact_us,name="contactus"),
]
