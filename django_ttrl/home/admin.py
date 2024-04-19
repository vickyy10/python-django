from django.contrib import admin
from .models import Departments ,Doctors,traill

from . models import Member
# Register your models here.

admin.site.register(Departments)

admin.site.register(Doctors)

admin.site.register(Member)

admin.site.register(traill)