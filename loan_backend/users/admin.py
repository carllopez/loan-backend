from django.contrib import admin

from .models import UserBalance


class UserBalanceAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__',]


admin.site.register(UserBalance, UserBalanceAdmin)
