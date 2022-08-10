from django.contrib import admin

# Register your models here.

from .models import Course, rc, Typee,Profile,Message

admin.site.register(rc)
admin.site.register(Course)
admin.site.register(Typee)
admin.site.register(Profile)
admin.site.register(Message)

