from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Journey(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="旅程名稱")
    start_date = models.DateField(blank=False, null=False, verbose_name="起始日期")
    end_date = models.DateField(blank=False, null=False, verbose_name="結束日期")
    creator = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE, verbose_name="創建者")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="最後修改時間")
