from django.contrib import admin
from todo_app.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'address', 'isMaried')
    list_filter = ('age', 'isMaried')
    search_fields =('name', 'email') 
    
admin.site.register(User, UserAdmin)