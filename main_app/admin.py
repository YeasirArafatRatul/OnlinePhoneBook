from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class ContactAdmin(ImportExportModelAdmin):
    list_display = ('name', 'designation', 'phone')
    list_filter = ('group',)
    list_editable = ('designation', 'phone')
    list_per_page = 5
    search_fields = ('name', 'group', 'designation', 'phone')


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
