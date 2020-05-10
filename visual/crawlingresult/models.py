from django.db import models
from django.contrib.auth import get_user_model
from Jobs.models import Job

# Create your models here.
class crawling_result(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    result = models.TextField()
        
    
    def __str__(self):
        return self.job.s_word + " 키워드 크롤링 결과"

class crawling_progress(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.job.s_word + " 키워드 진행 상황"