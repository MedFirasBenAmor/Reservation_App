from django.contrib import admin
from .models import User
from .models import Reservation
admin.site.register(Reservation)

admin.site.register(User)
# Register your models here.
