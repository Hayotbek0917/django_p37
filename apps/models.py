from django.db.models import Model, ForeignKey, CASCADE, TextField
from django.db.models.fields import CharField, IntegerField


class University(Model):
    name = CharField(max_length=255, null=True, blank=True)
    established_years = IntegerField(default=1935)
    description = TextField(default='')
    class Meta:
        verbose_name_plural = 'universities'

    def __str__(self):
        return f' {self.name}'


class Student(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    university = ForeignKey(University, CASCADE, null=True, blank=True)
    def full_name(self):
        return f'{self.first_name} {self.last_name}'