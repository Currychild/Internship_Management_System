from django.contrib import admin

# Register your models here.

from my_app.models import User

admin.site.register(User)
# admin.site.register(Teacher)
