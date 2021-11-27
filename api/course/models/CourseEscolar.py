import uuid

from django.db import models


class CourseEscolar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField("number of CourseEscolar", unique=True, null=False, blank=False)
    start_year = models.TextField('Start year', max_length=5)
    end_year = models.TextField('End year', max_length=5)

    class Meta:
        verbose_name='CourseEscolar'
        verbose_name_plural = 'CourseEscolar'

    def __str__(self) -> str:
        return f'start in {self.start_year} end in {self.end_year}'