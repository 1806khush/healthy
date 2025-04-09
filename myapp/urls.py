"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    path('index/', views.index, name='index'),
    path('adddoc/', views.adddoc, name='adddoc'),
    path('doctor/', views.doctor, name='doctor'),
    path('viewdoc/', views.viewdoc, name='viewdoc'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('changepass/', views.changepass, name='changepass'),
    path('changepass1/', views.changepass, name='changepass1'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('docindex/', views.docindex, name='docindex'),
    path('blog/', views.blog, name='blog-single'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('department/', views.department, name='department'),
    path('logout/', views.logout, name='logout'),
    path('forgotpass/', views.forgotpass, name='forgotpass'),
    path('otp/', views.otp, name='otp'),
    path('newpass/', views.newpass, name='newpass'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('docprofile/', views.docprofile, name='docprofile'),
    path('docabout/', views.docabout, name='docabout'),
    path('docservice/', views.docservice, name='docservice'),
    path('docdoctor/', views.docdoctor, name='docdoctor'),
    path('doccontact/', views.doccontact, name='doccontact'),
    path('perdepartment/', views.perdepartment, name='perdepartment'),
    path('docdepartment/', views.docdepartment, name='docdepartment'),
    path('docappoinment/', views.doctor_appointments, name='docappoinment'),
    path('docdetails/<int:doctor_id>/', views.docdetails, name='docdetails'),
    path('userdetails/<int:doctor_id>/', views.userdetails, name='userdetails'),
    path('userdoctor/', views.userdoctor, name='userdoctor'),
    path('updatedoc/<int:pk>/', views.updatedoc, name='updatedoc'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('book_appoinment/', views.book_appointment, name='appoinment'),
    path('appointment_detail/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('cardiology/', views.cardiology, name='cardiology'),
    path('dentist/', views.dentist, name='dentist'),
    path('homeopathy/', views.homeopathy, name='homeopathy'),
    path('neurology/', views.neurology, name='neurology'),
    path('pediatrics/', views.pediatrics, name='pediatrics'),
    path('traumatology/', views.traumatology, name='traumatology'),
    path('radiology/', views.radiology, name='radiology'),
    path('api/placeholder/<str:width>/<str:height>', views.placeholder_image, name='placeholder_image'),
]
