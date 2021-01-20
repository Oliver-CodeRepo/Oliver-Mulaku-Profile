from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','description']
    readonly_fields = ('name','email','subject','description')


admin.site.register(Contact, ContactAdmin)