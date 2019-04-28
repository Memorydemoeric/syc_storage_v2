# Generated by Django 2.2 on 2019-04-28 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefundOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rebate', models.IntegerField(default=0, verbose_name='折扣')),
                ('refund_actual_price', models.FloatField(default=0, verbose_name='退货金额')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('customer_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_info.CustomerInfo', verbose_name='客户信息')),
            ],
            options={
                'verbose_name_plural': '退货单',
                'verbose_name': '退货单',
                'db_table': 'syc_refund_order',
            },
        ),
        migrations.CreateModel(
            name='RefundDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.CharField(max_length=16, verbose_name='产品编号')),
                ('pro_count', models.IntegerField(default=0, verbose_name='数量')),
                ('refund_order_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.RefundOrder', verbose_name='退货单')),
            ],
            options={
                'verbose_name_plural': '退货单详情',
                'verbose_name': '退货单详情',
                'db_table': 'syc_refund_detail',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('actual_price', models.FloatField(default=0.0, verbose_name='提货金额')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('finish_time', models.DateTimeField(default=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'), verbose_name='完成时间')),
                ('order_comment', models.CharField(max_length=256, verbose_name='订单备注')),
                ('rebate', models.IntegerField(default=0, verbose_name='折扣')),
                ('order_status', models.IntegerField(choices=[(0, '已下单'), (1, '生产中'), (2, '出库结余'), (3, '完成')], default=0, verbose_name='订单状态')),
                ('payment_status', models.BooleanField(default=False, verbose_name='付款状态')),
                ('predict_freight', models.FloatField(default=0.0, verbose_name='估计运费')),
                ('is_selected', models.BooleanField(default=False, verbose_name='选择状态')),
                ('is_finished', models.BooleanField(default=False, verbose_name='完成状态')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('customer_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_info.CustomerInfo', verbose_name='客户信息')),
                ('order_handler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_info.UserInfo', verbose_name='用户信息')),
            ],
            options={
                'verbose_name_plural': '销售订单',
                'verbose_name': '销售订单',
                'db_table': 'syc_purchase_order',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.CharField(max_length=16, verbose_name='产品编号')),
                ('pro_count', models.IntegerField(default=0, verbose_name='数量')),
                ('pro_price', models.FloatField(default=0.0, verbose_name='金额')),
                ('purchase_order_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseOrder', verbose_name='订单信息')),
            ],
            options={
                'verbose_name_plural': '销售订单详情',
                'verbose_name': '销售订单详情',
                'db_table': 'syc_purchase_detail',
            },
        ),
    ]