from django.db import models
from api.core.models import BaseModel


class Grades(BaseModel):
    name = models.TextField('Grade name', max_length=100)

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

    def __str__(self) -> str:
        return f'{self.name}'
