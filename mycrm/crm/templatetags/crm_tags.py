__author__ = 'solin'
#自定义标签
from django import template
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime,timedelta
from django.core.exceptions import FieldDoesNotExist
register = template.Library()

@register.simple_tag
def render_contract(enrollment_obj):
    #返回model的verbose_name
    return enrollment_obj.enrolled_class.contract.template.format(course_name = enrollment_obj.enrolled_class,stu_name= enrollment_obj.customer.qq_name)
