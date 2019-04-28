from django.db import models

from purchase.models import RefundOrder
from storage.models import StorageOutOrder
from basic_info.models import CustomerInfo

# Create your models here.


class StatementOutputDetail(models.Model):
    origin_balance = models.FloatField(default=0.00, verbose_name='起始余额')
    income = models.FloatField(default=0.00, verbose_name='收款')
    balance = models.FloatField(default=0.00, verbose_name='余额')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    refund_order = models.ForeignKey(RefundOrder, on_delete=models.CASCADE, null=True,verbose_name='退货单')
    storage_out_order = models.ForeignKey(StorageOutOrder, on_delete=models.CASCADE, null=True, verbose_name='出库订单')
    customer_info = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True, verbose_name='客户信息')

    class Meta:
        db_table = 'syc_statement_output_detail'
        verbose_name = verbose_name_plural = '对账单详情'


class Cashflow(models.Model):
    FLOW_TYPE_NOMAL = 0
    FLOW_TYPE = (
        (0, '发货'),
        (1, '收款'),
        (2, '退货'),
    )
    flow_type = models.IntegerField(choices=FLOW_TYPE, default=FLOW_TYPE_NOMAL, verbose_name='类型')
    cash_change = models.FloatField(default=0.00, verbose_name='变动金额')
    balance = models.FloatField(default=0.00, verbose_name='余额')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    refund_order = models.ForeignKey(RefundOrder, on_delete=models.CASCADE, null=True,verbose_name='退货单')
    storage_out_order = models.ForeignKey(StorageOutOrder, on_delete=models.CASCADE, null=True, verbose_name='出库订单')
    customer_info = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True, verbose_name='客户信息')

    class Meta:
        db_table = 'syc_cashflow'
        verbose_name = verbose_name_plural = '现金流'
