from django.db import models

from purchase.models import PurchaseOrder
from basic_info.models import CustomerInfo, UserInfo

# Create your models here.


class StorageProductInfo(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_type = models.CharField(max_length=16, default='成品', verbose_name='类型')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    pro_unit_cost = models.FloatField(default=0.00, verbose_name='成本')
    pro_unit_price = models.FloatField(default=0.00, verbose_name='标准零售价')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'syc_storage_product_info'
        verbose_name = verbose_name_plural = '成品信息'


class StorageHalfInfo(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_type = models.CharField(max_length=16, default='半成品', verbose_name='类型')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    pro_unit_cost = models.FloatField(default=0.00, verbose_name='成本')
    pro_unit_price = models.FloatField(default=0.00, verbose_name='标准零售价')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'syc_storage_half_info'
        verbose_name = verbose_name_plural = '半成品信息'


class StorageInOrderHalf(models.Model):
    in_total_count = models.IntegerField(default=0, verbose_name='总数')
    in_created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    in_modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'syc_storage_in_order_half'
        verbose_name = verbose_name_plural = '半成品入库订单'


class StorageInDetailHalf(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    half_in_order = models.ForeignKey(StorageInOrderHalf, on_delete=models.CASCADE, verbose_name='半成品入库订单')

    class Meta:
        db_table = 'syc_storage_in_detail_half'
        verbose_name = verbose_name_plural = '半成品入库订单详情'


class StorageInOrderProduct(models.Model):
    in_total_count = models.IntegerField(default=0, verbose_name='总数')
    in_created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    in_modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'syc_storage_in_order_product'
        verbose_name = verbose_name_plural = '成品入库订单'


class StorageInDetailProduct(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    product_in_order = models.ForeignKey(StorageInOrderProduct, on_delete=models.CASCADE, verbose_name='成品入库订单')

    class Meta:
        db_table = 'syc_storage_in_detail_product'
        verbose_name = verbose_name_plural = '成品入库订单详情'


class StorageProductOperateRecord(models.Model):
    OPERATE_NORMAL = 0
    OPERATE_TYPE = (
        (0, '出库'),
        (1, '入库'),
        (2, '调整'),
        (3, '退货'),
        (4, '回滚'),
    )
    pro_operate_time = models.DateTimeField(auto_now_add=True, verbose_name='操作时间')
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_operate = models.IntegerField(choices=OPERATE_TYPE, default=OPERATE_NORMAL, verbose_name='操作类型')
    pro_old_count = models.IntegerField(default=0, verbose_name='原数量')
    pro_change_count = models.IntegerField(default=0, verbose_name='变化数量')
    pro_new_count = models.IntegerField(default=0, verbose_name='最终数量')

    class Meta:
        db_table = 'syc_storage_product_operate_record'
        verbose_name = verbose_name_plural = '成品库存操作记录'


class StorageHalfOperateRecord(models.Model):
    OPERATE_NORMAL = 0
    OPERATE_TYPE = (
        (0, '出库'),
        (1, '入库'),
        (2, '调整'),
        (3, '退货'),
        (4, '回滚'),
    )
    pro_operate_time = models.DateTimeField(auto_now_add=True, verbose_name='操作时间')
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_operate = models.IntegerField(choices=OPERATE_TYPE, default=OPERATE_NORMAL, verbose_name='操作类型')
    pro_old_count = models.IntegerField(default=0, verbose_name='原数量')
    pro_change_count = models.IntegerField(default=0, verbose_name='变化数量')
    pro_new_count = models.IntegerField(default=0, verbose_name='最终数量')

    class Meta:
        db_table = 'syc_storage_half_operate_record'
        verbose_name = verbose_name_plural = '半成品库存操作记录'


class StorageOutOrder(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    finish_time = models.DateTimeField(default=created_time, verbose_name='完成时间')
    price = models.FloatField(default=0.00, verbose_name='订单金额')
    actual_price = models.FloatField(default=0.00, verbose_name='提货金额')
    order_comment = models.CharField(max_length=256, verbose_name='订单备注')
    translation_expense = models.FloatField(default=0.00, verbose_name='运费')
    translation_comment = models.CharField(max_length=256, verbose_name='运费备注')
    rebate = models.IntegerField(default=0, verbose_name='折扣')
    payment_status = models.BooleanField(default=False, verbose_name='付款状态')
    is_delete = models.BooleanField(default=False, verbose_name='删除')
    purchase_order_info = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE, verbose_name='销售订单信息')
    customer_info = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, verbose_name='客户信息')
    order_handler = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户信息')

    class Meta:
        db_table = 'syc_storage_out_order'
        verbose_name = verbose_name_plural = '出库订单'


class StorageOutDetail(models.Model):
    pro_id = models.CharField(max_length=16, verbose_name='产品编号')
    pro_count = models.IntegerField(default=0, verbose_name='数量')
    pro_price = models.FloatField(default=0.00, verbose_name='金额')
    storage_out_order = models.ForeignKey(StorageOutOrder, on_delete=models.CASCADE, verbose_name='出库订单')

    class Meta:
        db_table = 'syc_storage_out_detail'
        verbose_name = verbose_name_plural = '出库订单详情'
