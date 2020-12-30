from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Workshop)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(NewCategory)