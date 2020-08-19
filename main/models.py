from django.db import models


# Create your models here.
class Corona(models.Model):
    global_table = models.CharField(max_length=99999)
    pakistan_table = models.CharField(max_length=99999)
    pak_stats = models.CharField(max_length=99999)
    global_stats = models.CharField(max_length=99999)


    class Meta:
        verbose_name_plural = 'Corona'