from django.db import models

# Create your models here.


class CustomerInfo(models.Model):
    location = models.CharField(max_length=128, verbose_name='地区')
    name = models.CharField(max_length=64, verbose_name='姓名')
    mobilephones = models.CharField(max_length=64, verbose_name='手机号')
    address = models.CharField(max_length=512, verbose_name='地址')
    phone = models.CharField(max_length=64, verbose_name='座机')
    default_rebate = models.IntegerField(default=100, verbose_name='折扣')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'syc_customer_info'
        verbose_name = verbose_name_plural = '客户信息'

    @classmethod
    def get_all_customer_info(cls):
        return cls.objects.filter(is_delete=False)

    @classmethod
    def get_appointed_customer_info(cls, condition):
        if condition:
            customer_list = [i for i in cls.get_all_customer_info() if condition in (i.location + i.name)]
            if customer_list:
                return customer_list
        return cls.get_all_customer_info()

    @classmethod
    def get_customer_info(cls, cust_id):
        try:
            customer_info = cls.objects.get(pk=int(cust_id))
        except Exception as e:
            print(e)
            return None
        else:
            return customer_info

    @classmethod
    def delete_customer_info(cls, cust_id):
        customer_info = cls.get_customer_info(cust_id)
        if customer_info:
            customer_info.is_delete = True
            customer_info.save()
        else:
            print('客户不存在...')


class CustomerRank(models.Model):
    order_count = models.IntegerField(default=0, verbose_name='订单数')
    balance = models.FloatField(default=0.00, verbose_name='余额')
    total_income =  models.FloatField(default=0.00, verbose_name='总金额')
    total_pro_count = models.IntegerField(default=0, verbose_name='总产品数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=True, verbose_name='是否删除')
    customer_info = models.OneToOneField(CustomerInfo, on_delete=models.CASCADE, verbose_name='客户信息')

    class Meta:
        db_table = 'syc_customer_rank'
        verbose_name = verbose_name_plural = '客户排名'


class UserInfo(models.Model):
    user_name = models.CharField(max_length=64, verbose_name='用户名')
    telephone_number = models.CharField(max_length=64, verbose_name='手机号')
    level = models.IntegerField(default=0, verbose_name='用户等级')
    comment = models.CharField(max_length=256, verbose_name='用户备注')
    password = models.CharField(max_length=128, verbose_name='密码')
    sign_in_token = models.CharField(max_length=128, verbose_name='token')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'syc_user_info'
        verbose_name = verbose_name_plural = '用户信息'
