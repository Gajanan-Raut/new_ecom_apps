from django.contrib import admin
from .models import student
from django.contrib import admin
# Register your models here.
# admin.site.register(student)

class studentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in student._meta.get_fields()]

admin.site.register(student, studentAdmin)