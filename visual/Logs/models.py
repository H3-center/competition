from django.conf import settings
from django.db import models
from django.utils import timezone
from Jobs.models import Job



class Log(models.Model):
    jobid=models.ForeignKey(Job,on_delete=models.CASCADE)
    executed_date=models.DateField()
    complited_date=models.DateField()


    def execute(self):
        self.executed_date=timezone.now()
        self.save()

# Create your models here.
