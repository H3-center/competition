from django.contrib import admin
from django.urls import path, include
from . import views

app_name='jobs'
urlpatterns = [
    path('', views.main, name="welcome"),   
    path('list/',views.job_list,  name="joblist"),
    path('tlist/',views.target_list , name="targetlist"),
    path('add/',views.job_list_form,  name="jobadd"),
    path('tadd/',views.target_list_form,  name="targetadd"),
    path('del/<int:id>/',views.job_del,  name="del"),
    path('tdel/<int:id>/',views.target_del,  name="tdel"),
    path('update/<int:id>/',views.job_list_update_form,  name="update"),
    path('tupdate/<int:id>/',views.target_list_update_form,  name="tupdate"),
    path('overview/',views.overview,name="overview"),
    path('chart/',views.chart,name="chart"),
    path('table/',views.table,name="table"),
    path('crawling/<int:id>/',views.crawling,name="crawling"),
]
