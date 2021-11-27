import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, identification_number, email, name, last_name, city, direction, phone_number, date_born,
                     gender, person_type, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            identification_number=identification_number,
            email=email,
            name=name,
            last_name=last_name,
            city=city,
            direction=direction,
            phone_number=phone_number,
            date_born=date_born,
            gender=gender,
            person_type=person_type,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, identification_number, email, name, last_name, city, direction, phone_number, date_born,
                    gender, person_type, password=None, **extra_fields):
        return self._create_user(identification_number, email, name, last_name, city, direction, phone_number,
                                 date_born, gender, person_type, password, False, False, **extra_fields)

    def create_superuser(self, identification_number, email, name, last_name, city, direction, phone_number, date_born,
                         gender, person_type, password=None, **extra_fields):
        return self._create_user(identification_number, email, name, last_name, city, direction, phone_number,
                                 date_born, gender, person_type, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDERS = (('M', 'Male'), ('F', 'Female'))
    PERSON_TYPES = (('S', 'Student'), ('T', 'Teacher'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identification_number = models.TextField('identification', max_length=30, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True, )
    name = models.TextField('Name', max_length=255)
    last_name = models.TextField('Last name', max_length=255, blank=True, null=True)
    city = models.TextField('city', max_length=30)
    direction = models.TextField('direction', max_length=50)
    phone_number = models.TextField('phone number', max_length=25, blank=True, null=True)
    date_born = models.DateField('date born', auto_now_add=False, auto_now=False)
    gender = models.TextField('gender', max_length=1, choices=GENDERS)
    person_type = models.TextField('person type', max_length=1, choices=PERSON_TYPES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['identification_number', 'name', 'last_name', 'phone_number', 'city', 'direction', 'date_born',
                       'gender', 'person_type']

    def __str__(self):
        return f'{self.name} {self.last_name}'