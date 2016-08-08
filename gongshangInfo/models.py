#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class company(models.Model):
    company_name=models.CharField('公司名称',max_length=30)
    person_name=models.CharField('人员名称',max_length=20)
    position=models.CharField('职位',max_length=15)

    class Meta:
        verbose_name='公司信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.company_name
