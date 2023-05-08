from django import forms
from rest_framework import serializers
from .models import Course
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class CourseSerializer(serializers.ModelSerializer):
#
#     # 如果想得到讲师的名字，将用户的名称序列化
#     teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段 只读
#     class Meta:
#         model = Course
#         # exclude = ('id', )  # 排除某些元素
#         # fields = ("name", "introduction")
#         fields = '__all__'

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'introduction', 'teacher', 'price', 'created_at', 'updated_at')
