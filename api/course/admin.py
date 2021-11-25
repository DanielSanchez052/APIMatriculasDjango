from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.course.models.CourseEscolar import CourseEscolar
from api.course.models.Grades import Grades
from api.course.models.Course import Course
from api.course.models.StudentCourse import StudentCourse


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    pass

@admin.register(Grades)
class GradesAdmin(ImportExportModelAdmin):
    pass

@admin.register(CourseEscolar)
class CourseEscolar(ImportExportModelAdmin):
    pass

@admin.register(StudentCourse)
class StudentCourseAdmin(ImportExportModelAdmin):
    pass