from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Поля модели
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True
    )
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_goal = models.CharField(
        max_length=50,
        choices=[
            ('Lose Weight', 'Lose Weight'),
            ('Build Muscle', 'Build Muscle'),
            ('Stay Fit', 'Stay Fit')
        ],
        blank=True
    )

    # Поле email становится уникальным идентификатором
    USERNAME_FIELD = 'email'

    # Поля, обязательные для суперпользователя
    REQUIRED_FIELDS = ['username', 'age', 'gender', 'weight', 'height', 'fitness_goal']

    def __str__(self):
        return self.email
