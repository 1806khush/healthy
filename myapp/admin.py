from django.contrib import admin
from .models import User
from .models import Doctor
from django import forms
from .models import Booking
# from .models import Booking
# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Booking)
