from django.db import models

# Create your models here.


class PlanOrder(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'syc_plan_order'
        verbose_name = verbose_name_plural = '生产安排'


class PlanDetail(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    plan_order = models.ForeignKey(PlanOrder, on_delete=models.CASCADE, verbose_name='生产安排')

    class Meta:
        db_table = 'syc_plan_detail'
        verbose_name = verbose_name_plural = '生产安排详情'
