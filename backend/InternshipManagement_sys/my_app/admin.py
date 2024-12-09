from django.contrib import admin

# Register your models here.

from .models import User, Teacher

admin.site.register(User)
admin.site.register(Teacher)
