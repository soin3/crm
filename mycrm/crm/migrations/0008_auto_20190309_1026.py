# Generated by Django 2.1.2 on 2019-03-09 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20190309_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='crm.Tag', verbose_name='标签'),
        ),
    ]