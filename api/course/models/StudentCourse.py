import uuid

from django.db import models

class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField("number of StudentCourse", unique=True, null=False, blank=False)
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, null=True, related_name='courses')
    course = models.ForeignKey('course.Course',on_delete=models.CASCADE)
    course_escolar = models.ForeignKey('course.CourseEscolar', on_delete=models.CASCADE)

    class Meta:
        verbose_name='StudentCourse'
        verbose_name_plural = 'StudentCourse'

    def __str__(self) -> str:
        return f'{self.user.__str__()} curso: {self.course.__str__()}'
