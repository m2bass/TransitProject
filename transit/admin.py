from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Agency, Routes, Trips, Stops, StopTimes

admin.site.register(Agency)
admin.site.register(Routes)
admin.site.register(Trips)
admin.site.register(Stops)
admin.site.register(StopTimes)
