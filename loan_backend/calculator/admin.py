from django.contrib import admin

from .models import Operation, Record


class OperationAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__',]


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'operation', 'user', 'date']
    readonly_fields = ['date']


admin.site.register(Operation, OperationAdmin)
admin.site.register(Record, RecordAdmin)
