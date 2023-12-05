from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
                    ('Personal Informations', {
                        'fields': ('firstname', 'lastname', 'age','gender','address','profile_image')}),
                    ('School Details', {
                        'classes': ('wide',),'fields': ('school_name', 'standard'),}),
                    ('Parent Details', 
                        {'classes': ('wide',),'fields': ('fathers_name','mother_name','parent_contact_number'),}),
                )
    
    list_display=('full_name','age','gender','address')
    search_fields = ("firstname",)
    def full_name(self, obj):
        return obj.firstname + " " + obj.lastname
  
admin.site.register(Student, StudentAdmin)
admin.site.unregister(Group)
