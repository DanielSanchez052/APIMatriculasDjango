from django.contrib import admin
from django.contrib.sessions.models import Session
from import_export.admin import ImportExportModelAdmin

from api.user.models.User import User
from api.user.models.Teacher import Teacher
from api.user.models.Department import Department


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Session)

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    pass


