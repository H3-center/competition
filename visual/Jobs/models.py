from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import MyUser

class Target_list(models.Model):
    media=models.CharField(max_length=200)
    crawling_url=models.URLField(max_length=300)
    input_col=models.TextField() ## , seperater로 데이터를 넣고 구분 (프론트에서 한번 백에서 한번 벨리데이션 체크)

    def __str__(self):
        return self.media

class Job(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    s_word=models.CharField(max_length=255)
    media=models.ForeignKey(Target_list,on_delete=True)
    active_status=models.IntegerField()
    executed_date=models.DateField()
    complited_date=models.DateField()
    t_st_date=models.DateField()
    t_end_date=models.DateField()

    def execute(self):
        self.executed_date=timezone.now()
        self.save()

    






# Create your models here.
