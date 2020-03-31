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


class Target_list(models.Model):
    media=models.CharField(max_length=200)
    crawling_url=models.URLField(max_length=300)
    input_col=models.TextField() ## , seperater로 데이터를 넣고 구분 (프론트에서 한번 백에서 한번 벨리데이션 체크)




# Create your models here.
