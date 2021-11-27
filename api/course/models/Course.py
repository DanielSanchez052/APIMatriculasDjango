from django.db import models
from api.core.models import BaseModel


class Course(BaseModel):
    TYPE = (('B', 'Basic'), ('R', 'Required'), ('O', 'Optional'))

    number = models.IntegerField("number of Course", unique=True, null=False, blank=False)
    name = models.TextField("name", max_length=100)
    credit = models.IntegerField('credits')
    type = models.TextField('type', max_length=1, choices=TYPE)
    course = models.SmallIntegerField('course')
    quarter = models.SmallIntegerField('semestre')
    teacher = models.ForeignKey('user.Teacher', on_delete=models.CASCADE, blank=True, null=True)
    grade = models.ForeignKey('course.Grades', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self) -> str:
        return f'{self.name}'
