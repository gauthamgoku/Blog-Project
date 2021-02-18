from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import  Article_Comment
from .models import  Articles

admin.site.register(Articles)
admin.site.register(Article_Comment)
