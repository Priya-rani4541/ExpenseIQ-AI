from django.contrib import admin

# Register your models here.
from .models import ImportLog

admin.site.register(ImportLog)