from django.contrib import admin
from .models import AdminUser, Books

admin.site.register(AdminUser)
admin.site.register(Books)

