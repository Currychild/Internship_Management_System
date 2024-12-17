from django.contrib.auth.hashers import check_password
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from my_app.serializers import UserSerializer, TeacherInfoSerializer, CompanyTeacherSerializer

from .models import Academy, Major, Teacher, Class, Student, Announcement, Company
from .models import CompanyTeacher, IpActivity, IpApplication, IpJob, IpSummary, IpWeekly, User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TeacherInfoViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherInfoSerializer

class CompanyTeacherViewSet(viewsets.ModelViewSet):
    queryset = CompanyTeacher.objects.all()
    serializer_class = CompanyTeacherSerializer

from .serializers import LoginSerializer
class LoginView(APIView):
    def post(self, request):
        # 1.反序列化前端传递的数据
        serializer = LoginSerializer(data=request.data)

        print(request.data)  # DBG测试请求体数据


        if serializer.is_valid():
            print(serializer.validated_data)
            u_id = serializer.validated_data['u_id']
            u_password = serializer.validated_data['u_password']

            # 2.查找数据库相应信息
            try:
                user = User.objects.get(u_id=u_id)
            except User.DoesNotExist:
                return Response({"message": "Invalid username or password"}, status = status.HTTP_400_BAD_REQUEST)

            # 3.验证密码：
            if check_password(u_password,user.password):
                # 登陆成功
                return Response({"message":"Login successful", "success":True}, status = status.HTTP_200_OK)
            else:
                # 密码错误
                return Response({"message": "Invalid username or password"},status=status.HTTP_400_BAD_REQUEST)
        else:
            # 序列化数据不合法
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)