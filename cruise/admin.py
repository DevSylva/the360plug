from django.contrib import admin
# username == plug
# password == 360
# Register your models here.
from .models import *

admin.site.register(Message)
admin.site.register(Service)
