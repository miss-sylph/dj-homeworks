
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)