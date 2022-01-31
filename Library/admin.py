from django.contrib import admin

from Library.models import Clientele, Password, Ebook, Journal


class ClienteleAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'clientele_id', 'sex', 'phone_no', 'email', 'role')


class PasswordAdmin(admin.ModelAdmin):
    list_display = ('clientele', 'recovery_password', 'time', 'is_active')


class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'description', 'programme', 'date', 'file')


class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'description', 'date', 'file')


admin.site.register(Clientele, ClienteleAdmin)
admin.site.register(Password, PasswordAdmin)
admin.site.register(Ebook, EbookAdmin)
admin.site.register(Journal, JournalAdmin)
