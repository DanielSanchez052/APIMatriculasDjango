import uuid

from django.db import models

from api.user.models.User import User
from api.course.models.CourseEscolar import CourseEscolar
from api.course.models.Course import Course


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='courses')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    course_escolar = models.ForeignKey(CourseEscolar, on_delete=models.CASCADE)

    class Meta:
        verbose_name='StudentCourse'
        verbose_name_plural = 'StudentCourse'

    def __str__(self) -> str:
        return f'{self.user.__str__()} curso: {self.course.__str__()}'
