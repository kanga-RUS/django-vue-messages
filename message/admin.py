from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]
    list_filter = ['date', ]

    class Meta:
        model = Message


admin.site.register(Message, MessageAdmin)
