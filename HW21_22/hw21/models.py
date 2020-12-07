from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ['first_name', ]
        unique_together = ['first_name', 'last_name']
        db_table = 'person'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.

# class Pupil(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     age = models.PositiveSmallIntegerField()
#     profession = models.CharField(max_length=255, null=True)
#
#     class Meta:
#         ordering = ['first_name',]
#         unique_together = ['first_name', 'last_name']
#         db_table = 'pupil'
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
