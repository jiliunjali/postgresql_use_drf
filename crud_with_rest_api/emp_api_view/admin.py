from django.contrib import admin
from .models import Employee
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
# it is for how employee will look in admin inteface
class EmployeeAdmin(BaseUserAdmin):

    list_display = ["id","email", "fullname", "emp_code","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["fullname","mobile"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []
    
admin.site.register(Employee, EmployeeAdmin)
