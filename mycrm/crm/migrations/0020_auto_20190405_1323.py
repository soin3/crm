# Generated by Django 2.1.7 on 2019-04-05 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20190403_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_access_my_course', '可以访问我的课程'), ('can_access_customer_list', '可以访问客户列表'), ('can_access_customer_detail', '可以访问客户详细'))},
        ),
    ]
