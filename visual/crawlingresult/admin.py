from django.contrib import admin
from .models import crawling_result, crawling_progress
# Register your models here.
admin.site.register(crawling_result)
admin.site.register(crawling_progress)