from django.contrib import admin

# Register your models here.
from customer.models import User

admin.site.register(User)