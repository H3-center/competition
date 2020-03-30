from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Job(models.Model):
    
    s_word=models.CharField(max_length=255)
    media=models.CharField(max_length=200)
    active_status=models.IntegerField()
    executed_date=models.DateField()
    complited_date=models.DateField()
    t_st_date=models.DateField()
    t_end_date=models.DateField()

    def execute(self):
        self.executed_date=timezone.now()
        self.save()

# Create your models here.
