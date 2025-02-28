from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(ActivityLog)
admin.site.register(Message)