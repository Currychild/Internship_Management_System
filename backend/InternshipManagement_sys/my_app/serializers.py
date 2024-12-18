# 序列化器
import base64
from random import choices
from typing import Dict, Any

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from .models import User, Teacher, Academy, Major, Class
from .models import Student, Announcement, Company, CompanyTeacher
from .models import IpActivity, IpApplication, IpJob, IpSummary, IpWeekly

#有bug，无法实现转换，即queryset是有内容的，但是传入UserSerializer中的时候，返回的json格式变成了{}，内不包含内容。
class UserSerializer(serializers.ModelSerializer):
    u_photo = serializers.SerializerMethodField() #自定义方法字段

    """用户数据序列化器"""
    class Meta:
        model = User
        fields = ['u_id', 'u_name', 'u_type', 'u_tel', 'u_photo', 'u_status']

    def get_u_photo(self,obj):
        #将二进制图像数据转为 Base64 编码字符串
        #注意：这样会使得文件大小变大，但是不用再单独请求图片文件，后续可进一步优化
        if obj.u_photo:
            return base64.b64encode(obj.u_photo).decode('utf-8')
        return None

class TeacherInfoSerializer(serializers.ModelSerializer):
    """校内导师数据序列化器"""

    class Meta:
        model = Teacher
        fields = '__all__'

class AcademyInfoSerializer(serializers.ModelSerializer):
    """学院信息数据序列化"""

    class Meta:
        model = Academy
        fields = '__all__'

class MajorInfoSerializer(serializers.ModelSerializer):
    """专业信息数据数列话器"""

    class Meta:
        model = Major
        fields = '__all__'

class ClassInfoSerializer(serializers.ModelSerializer):
    """班级信息序列化器"""

    class Meta:
        model = Class
        fields = '__all__'

class StudentInfoSerializer(serializers.ModelSerializer):
    """学生信息序列化器"""
    user = UserSerializer(source= 's_id') #嵌套User序列化器
    c_id = serializers.StringRelatedField() #显示班级名称等相关字段

    class Meta:
        model = Student
        fields = ['s_grade', 's_state', 'user', 'c_id']

class AnnouncementSerializer(serializers.ModelSerializer):
    """公告序列化器"""

    class Meta:
        model = Announcement
        fields = '__all__'

class CompanyInfoSerializer(serializers.ModelSerializer):
    """公司信息序列化器"""

    class Meta:
        model = Company
        fields = '__all__'

class CompanyTeacherSerializer(serializers.ModelSerializer):
    """企业导师信息序列器"""

    class Meta:
        model = CompanyTeacher
        fields = '__all__'

class IpActivitySerializer(serializers.ModelSerializer):
    """实习活动序列化器"""

    class Meta:
        model = IpActivity
        fields = '__all__'

class IpApplicationSerializer(serializers.ModelSerializer):
    """实习申请序列器"""

    class Meta:
        model = IpApplication
        fields = '__all__'

class IpJobSerializer(serializers.ModelSerializer):
    """实习工作序列化器"""

    class Meta:
        model = IpJob
        fields = '__all__'

class IpSummarySerializer(serializers.ModelSerializer):
    """实习总结序列化器"""

    class Meta:
        model = IpSummary
        fields = '__all__'

class IpWeeklySerializer(serializers.ModelSerializer):
    """实习周报序列化器"""

    class Meta:
        model = IpWeekly
        fields = '__all__'


#详细功能区分：

# 重写 TokenObtainPairSerializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        """payload里面添加数据"""
        token = super().get_token(user)
        #添加信息
        token['u_id'] = user.u_id
        # token['username'] = user.username
        token['u_type'] = user.u_type
        return token

    # 重写Token方法
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        #添加额外的返回信息给前端用于扔着
        data['u_id'] = user.u_id
        data['username'] = user.username
        data['u_type'] = user.u_type
        return data

#登录信息匹配序列化器
# class LoginSerializer(serializers.ModelSerializer):
#     "登录序列化器"
#     class Meta:
#         model = User
#         fields = ['u_id', 'u_type']  # 只返回 u_id 和 u_type