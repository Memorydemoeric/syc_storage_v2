# Generated by Django 2.2 on 2019-04-28 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '生产安排',
                'verbose_name': '生产安排',
                'db_table': 'syc_plan_order',
            },
        ),
        migrations.CreateModel(
            name='PlanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.CharField(max_length=16, verbose_name='产品编号')),
                ('pro_count', models.IntegerField(default=0, verbose_name='数量')),
                ('plan_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.PlanOrder', verbose_name='生产安排')),
            ],
            options={
                'verbose_name_plural': '生产安排详情',
                'verbose_name': '生产安排详情',
                'db_table': 'syc_plan_detail',
            },
        ),
    ]
