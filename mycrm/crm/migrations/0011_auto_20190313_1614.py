# Generated by Django 2.1.2 on 2019-03-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20190313_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='qq',
            field=models.CharField(help_text='QQ号必须唯一', max_length=64, unique=True, verbose_name='qq号'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='qq_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='qq名称'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='source',
            field=models.SmallIntegerField(choices=[(0, '转介绍'), (1, 'qq'), (2, '微信'), (3, '官方论坛'), (4, '网上搜索'), (5, '其他')], verbose_name='来源'),
        ),
    ]