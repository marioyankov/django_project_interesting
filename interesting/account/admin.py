from django.contrib import admin

# Register your models here.
from account.models import UserProfile


class ViewUser(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(UserProfile, ViewUser)
