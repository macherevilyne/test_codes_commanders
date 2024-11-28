from django.contrib import admin
from .models import UserProfile, Orders
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Orders)
