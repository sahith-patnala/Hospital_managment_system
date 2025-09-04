from django.contrib import admin

# Register your models here.

from .models import Appointment,data

# Register your models here.


admin.site.register(Appointment)
admin.site.register(data)

