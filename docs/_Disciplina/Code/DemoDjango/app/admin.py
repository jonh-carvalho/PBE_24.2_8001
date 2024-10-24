from django.contrib import admin
from .models import Employee,Department


admin.site.register(Employee) 
admin.site.register(Department) # Register your models here.

