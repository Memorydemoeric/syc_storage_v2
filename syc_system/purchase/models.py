from django.db import models

from basic_info.models import CustomerInfo, UserInfo

# Create your models here.


class PurchaseOrder(models.Model):
    ORDER_STATUS_NOMAL = 0
    ORDER_STATUS = (
        (0, '已下单'),
        (1, '生产中'),
        (2, '出库结余'),
        (3, '完成'),
    )
    price = models.FloatField(default=0.00, verbose_name='订单金额')
    actual_price = models.FloatField(default=0.00, verbose_name='提货金额')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    finish_time = models.DateTimeField(default=created_time, verbose_name='完成时间')
    order_comment = models.CharField(max_length=256, verbose_name='订单备注')
    rebate = models.IntegerField(default=0, verbose_name='折扣')
    order_status = models.IntegerField(choices=ORDER_STATUS, default=ORDER_STATUS_NOMAL, verbose_name='订单状态')
    payment_status = models.BooleanField(default=False, verbose_name='付款状态')
    predict_freight = models.FloatField(default=0.00, verbose_name='估计运费')
    is_selected = models.BooleanField(default=False, verbose_name='选择状态')
    is_finished = models.BooleanField(default=False, verbose_name='完成状态')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    customer_info = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, verbose_name='客户信息')
    order_handler = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户信息')

    class Meta:
        db_table = 'syc_purchase_order'
        verbose_name = verbose_name_plural = '销售订单'


class PurchaseDetail(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    pro_price = models.FloatField(default=0.00, verbose_name='金额')
    purchase_order_info = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,verbose_name='订单信息')

    class Meta:
        db_table = 'syc_purchase_detail'
        verbose_name = verbose_name_plural = '销售订单详情'


class RefundOrder(models.Model):
    rebate = models.IntegerField(default=0, verbose_name='折扣')
    refund_actual_price = models.FloatField(default=0, verbose_name='退货金额')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    customer_info = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, verbose_name='客户信息')

    class Meta:
        db_table = 'syc_refund_order'
        verbose_name = verbose_name_plural = '退货单'


class RefundDetail(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    refund_order_info = models.ForeignKey(RefundOrder, on_delete=models.CASCADE, verbose_name='退货单')

    class Meta:
        db_table = 'syc_refund_detail'
        verbose_name = verbose_name_plural = '退货单详情'
