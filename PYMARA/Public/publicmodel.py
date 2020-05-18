from django.db import models

class PublicModel(models.Model):
    create_time = models.TimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.TimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True