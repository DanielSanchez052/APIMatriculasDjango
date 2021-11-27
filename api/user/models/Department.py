from django.db import models
from api.core.models import BaseModel


class Department(BaseModel):
    number = models.IntegerField("number of department",unique=True, null=False, blank=False)
    name = models.TextField('department name', max_length=50)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self) -> str:
        return f'{self.name}'
