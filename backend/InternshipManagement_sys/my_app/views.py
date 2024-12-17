from functools import partial
from os import access
from pickle import FALSE

from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

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

        if serializer.is_valid():
            u_id = serializer.validated_data['u_id']
            u_password = serializer.validated_data['u_password']

            # 2.查找数据库相应信息
            try:
                user = User.objects.get(u_id=u_id)
            except User.DoesNotExist:
                return Response({"message": "Invalid username or password"}, status = status.HTTP_400_BAD_REQUEST)

            # 3.验证密码：
            if check_password(u_password,user.u_password):
                # 生成 JWT Token
                refresh = AccessToken.for_user(user) # 为用户生成JWT的 Refresh Token
                access_token = str(refresh.access_token) # 获取 Access Token

                #返回 Token 给前端
                return Response({
                    "message": "Login successful",
                    "success": True,
                    "access_token": access_token,
                    "refresh_token": str(refresh),
                }, status=status.HTTP_200_OK)
            else:
                # 密码错误
                return Response({"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 序列化数据不合法
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


from .serializers import StudentInfoSerializer
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 只返回当前登录学生的数据
        return Student.objects.filter(s_id=self.request.user)

    @action(detail=False, methods=['get'], url_path='me')
    def get_student_info(self, request):
        """查询学生个人信息（返回除密码外的）"""
        student = Student.objects.get(s_id=request.user.u_id)
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    @action(detail=False, methods=['patch'], url_path='update')
    def update_student_info(self, request):
        """学生个人信息修改"""
        student = Student.objects.get(s_id=request.user)
        serializer = self.get_serializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='change-password')
    def change_password(self, request):
        """学生修改密码（验证+修改新密码）"""
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        # 检查原始密码是否正确
        if not check_password(old_password, user.u_password):
            return Response({'detail': '原密码错误'},status=status.HTTP_400_BAD_REQUEST)

        # 确认新密码与确认密码一致
        if new_password != confirm_password:
            return Response({'detail': '新密码和确认密码不一致'}, status=status.HTTP_400_BAD_REQUEST)

        # 更新密码
        user.u_password = make_password(new_password)
        user.save()

        return Response({'detail': '密码修改成功'}, status=status.HTTP_200_OK)