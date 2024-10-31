from django.contrib import admin

# Register your models here.
from .models import Register
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','confirm_password']