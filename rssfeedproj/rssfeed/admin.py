"""
Admin
"""
from django.contrib import admin
from .models import RssCache, RssCacheEsp

# Register your models here.
admin.site.register(RssCache)
admin.site.register(RssCacheEsp)
