# Generated by Django 2.1.2 on 2019-02-19 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.SmallIntegerField(choices=[(0, '面授(脱产)'), (1, '面授(周末)'), (2, '随到随学网络')], default=0, verbose_name='班级类型')),
                ('semester', models.PositiveSmallIntegerField(verbose_name='学期')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='校区')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='课程名')),
                ('price', models.PositiveSmallIntegerField(verbose_name='课程价格')),
                ('outline', models.TextField(verbose_name='课程大纲')),
                ('period', models.IntegerField(verbose_name='课程周期(Month)')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='第几节课（天）')),
                ('has_homework', models.BooleanField(default=True, verbose_name='本节有作业')),
                ('homework_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='作业标题')),
                ('homework_content', models.TextField(blank=True, null=True, verbose_name='作业内容')),
                ('outline', models.TextField(verbose_name='本节课程大纲')),
                ('date', models.DateField(auto_now_add=True, verbose_name='上课日期')),
                ('from_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='班级')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('qq', models.CharField(help_text='QQ号必须唯一', max_length=64, unique=True)),
                ('qq_name', models.CharField(blank=True, max_length=64, null=True)),
                ('source', models.SmallIntegerField(choices=[(0, '转介绍'), (1, 'qq'), (2, '微信'), (3, '官方论坛'), (4, '网上搜索'), (5, '其他')])),
                ('referral_from', models.CharField(blank=True, max_length=64, null=True, verbose_name='转介绍人qq')),
                ('content', models.TextField(verbose_name='咨询详情')),
                ('date', models.DateField(auto_now_add=True, verbose_name='咨询日期')),
                ('consult_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='咨询课程')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='跟进内容')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
                ('status', models.IntegerField(choices=[(1, '近期无报名计划'), (2, '2个月内报名'), (3, '1个月内报名'), (4, '2周内报名'), (5, '1周内报名'), (6, '2天内报名'), (7, '已报名'), (8, '已交全款')], help_text='选择客户此时的状态', verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_agreed', models.BooleanField(verbose_name='学员已同意合同')),
                ('contract_approved', models.BooleanField(help_text='合同已审核', verbose_name='审批通过')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_fee', models.IntegerField(default=0, verbose_name='费用数额')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='交款日期')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(choices=[(0, '已签到'), (1, '迟到'), (2, '缺勤'), (3, '早退')], default='checked', max_length=64, verbose_name='上课纪录')),
                ('score', models.IntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (70, 'B-'), (60, 'C+'), (50, 'C'), (40, 'C-'), (-50, 'D'), (0, 'N/A'), (-100, 'COPY'), (-1000, 'FAIL')], default=0, verbose_name='本节成绩')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='第几天课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='学员')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('roles', models.ManyToManyField(blank=True, null=True, to='crm.Role', verbose_name='用户角色')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='consultant',
            field=models.ForeignKey(help_text='谁签的单就选谁', on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='负责老师'),
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrolled_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='所报班级'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='跟踪人'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='所咨询客户'),
        ),
        migrations.AddField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together={('course_record', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('customer', 'enrolled_class')},
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together={('from_class', 'day_num')},
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together={('branch', 'course', 'semester')},
        ),
    ]