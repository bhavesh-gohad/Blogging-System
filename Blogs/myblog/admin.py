from django.contrib import admin
from .models import Post,Contact,Profile
# Register your models here.
@admin.register(Post)


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','published','author']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bio','profile_pic']