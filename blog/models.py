from django.db import models
from django.db.models.expressions import F
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=24, null=False)
    content = models.TextField(max_length=200, null=False)
    create_date = models.DateField(default=timezone.get_current_timezone)
    date = models.DateTimeField(null=False)


def publish(self):
    self.date = timezone.now()
    self.save()


def __str__(self) -> str:
    return self.author.username + ' ' + self.title
