from django.contrib import admin
from .models import service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

admin.site.register(service,ServiceAdmin)

