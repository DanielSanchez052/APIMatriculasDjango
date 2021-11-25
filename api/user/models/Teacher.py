import uuid

from django.db import models

from .Department import Department
from .User import User


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.person.name} {self.person.last_name} departamento: {self.department.name}'
