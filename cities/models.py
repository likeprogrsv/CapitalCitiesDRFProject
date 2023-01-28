from django.db import models
from django.contrib.auth.models import User


class Cities(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    continent = models.ForeignKey('Continent', on_delete=models.PROTECT,
                                  null=True)
    user = models.ForeignKey(User, verbose_name="user",
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Continent(models.Model):
    continent_name = models.CharField(max_length=150, db_index=True)

    def __str__(self) -> str:
        return self.continent_name
