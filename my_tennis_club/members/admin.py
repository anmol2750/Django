from django.contrib import admin
from .models import member

class member_admin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phoneno')
    prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(member,member_admin)


