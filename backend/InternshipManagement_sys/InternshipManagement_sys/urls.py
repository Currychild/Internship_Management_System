"""
URL configuration for InternshipManagement_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from my_app import views
from my_app.views import StudentViewSet, CustomTokenObtainPairView

# from my_app.views import LoginView

#配置路由器
router = DefaultRouter()
#注册视图集
# router.register(r'users',views.UserViewSet)
# router.register(r'teachers',views.TeacherInfoViewSet)
# router.register(r'companyteachers',views.CompanyTeacherViewSet)
#router.register(r'students', StudentViewSet, basename='student')

#设置api接口文档：
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), #权限类
)

urlpatterns = [
    path('admin/', admin.site.urls), # django后端管理

    # path('login/', LoginView.as_view(), name='login'), # 登录功能
    path('api/', include(router.urls)), # 加载前面配置的路由器
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # 获取 JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新 JWT token

    # 你的 API 路由
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),  # Swagger UI 文档
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),  # ReDoc UI 文档
]


# urlpatterns += router.urls