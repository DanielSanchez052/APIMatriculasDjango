import uuid

from django.db import models


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField("number of Teacher", unique=True, null=False, blank=False)
    person = models.ForeignKey('user.User', on_delete=models.CASCADE)
    department = models.ForeignKey('user.Department', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.person.name} {self.person.last_name} departamento: {self.department.name}'
