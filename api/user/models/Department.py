from django.db import models
from api.core.models import BaseModel


class Department(BaseModel):
    name = models.TextField('department name', max_length=50)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self) -> str:
        return f'{self.name}'
