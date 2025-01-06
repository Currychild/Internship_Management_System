from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
# from users.models import User
# Create your models here.
# Academy Model (for the 'academy' table)

# 重写manager
class UserManager(BaseUserManager):
    def create_user(self, u_tel, password=None, u_type=1, u_photo=None):
        """
        创建一个普通用户
        """
        if not u_tel:
            raise ValueError('用户必须提供电话')

        # 创建用户对象
        user = self.model(
            u_tel=u_tel,
            u_type=u_type,
            u_photo=u_photo,
        )

        # 如果没有提供密码，则使用默认密码
        if password:
            user.set_password(password)  # 设置密码
        else:
            user.set_password('1234567')  # 使用默认密码

        user.save(using=self._db)  # 保存到数据库

        # 自动生成 username
        self._generate_username(user)

        return user

    def create_superuser(self, u_tel, password=None, u_type=0, u_photo=None):
        """
        创建超级管理员用户
        """
        user = self.create_user(
            u_tel=u_tel,
            password=password,
            u_type=u_type,
            u_photo=u_photo,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def _generate_username(self, user):
        """
        根据 u_type 和 u_id 自动生成 username
        """
        if user.u_type == 0:  # 管理员
            user.username = f'admin{user.u_id}'
        elif user.u_type == 1:  # 学生
            user.username = f'student{user.u_id}'
        elif user.u_type == 2:  # 班主任
            user.username = f'teacher{user.u_id}'
        elif user.u_type == 3:  # 企业导师
            user.username = f'Cteacher{user.u_id}'

        user.save(using=self._db)  # 保存更新后的 username

# 用户表 User Model
#注释的为AbstractUser默认属性
class User(AbstractUser):
    u_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    # username = models.USERNMEE(max_length=20, verbose_name='用户名（姓名）')
    # password = models.CharField(max_length=20, default='123456', verbose_name='密码')
    u_type = models.IntegerField(verbose_name='用户类型', choices=[(0, '管理员'), (1, '学生'), (2, '班主任'), (3, '企业导师')])
    u_tel = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    u_photo = models.BinaryField(null=True, blank=True, verbose_name='照片')
    # is_active = models.IntegerField(default=0, verbose_name='激活状态，0为未激活，1为已激活')

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = '用户'


# 学生表 Student Model
class Student(models.Model):
    s_id = models. OneToOneField('User', on_delete=models.CASCADE, verbose_name='学生ID', primary_key=True)
    c_id = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name='班级ID',null=True, blank=True)
    s_grade = models.CharField(max_length=20, verbose_name='学生年级')
    s_state = models.BinaryField(verbose_name='是否实习，0为否，1为是')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = '学生'


# 老师表 Teacher Model
class Teacher(models.Model):
    t_id = models. OneToOneField('User', on_delete=models.CASCADE, verbose_name='老师ID',primary_key=True)
    c_id = models.ForeignKey('Class',on_delete=models.CASCADE,verbose_name='管理班级ID',null=True, blank=True)
    t_type = models.IntegerField(verbose_name='是否班主任', choices=[(0, '不是班主任'), (1, '是班主任')])

    class Meta:
        db_table = 'teacher'
        verbose_name = '校内导师'
        verbose_name_plural = '校内导师'


# 企业表 Company Model
class Company(models.Model):
    co_id = models.IntegerField(primary_key=True, verbose_name='企业ID')
    #co_contacts_id = models.ForeignKey('CompanyTeacher',on_delete=models.CASCADE,verbose_name='企业联系人ID',null=True, blank=True)
    #企业联系人不一定是企业老师，这里进行修改
    co_contacts = models.CharField(max_length=20, verbose_name='企业联系人')
    co_name = models.CharField(max_length=20, verbose_name='企业名称')
    co_address = models.CharField(max_length=45, verbose_name='企业地址')
    co_scale = models.IntegerField(verbose_name='企业规模')

    class Meta:
        db_table = 'company'
        verbose_name = '企业'
        verbose_name_plural = '企业'


# 企业导师表 CompanyTeacher Model
class CompanyTeacher(models.Model):
    cot_id = models. OneToOneField('User', on_delete=models.CASCADE, verbose_name='企业导师ID', primary_key=True)
    co_id = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='企业ID',null=True, blank=True)
    act_id = models.ForeignKey('IpActivity',on_delete=models.CASCADE,null=True, blank=True, verbose_name='管理的实习活动ID')
    cot_title = models.CharField(max_length=45, verbose_name='职称')

    class Meta:
        db_table = 'company_teacher'
        verbose_name = '企业导师'
        verbose_name_plural = '企业导师'


# 学院表 Academy Model
class Academy(models.Model):
    a_id = models.IntegerField(primary_key=True, verbose_name='院系ID')
    #a_dean_id = models.ForeignKey('Teacher',on_delete=models.CASCADE,verbose_name='院长ID',null=True, blank=True)
    #院长不一定是老师，这里进行修改
    a_dean = models.CharField(max_length=20, verbose_name='院长')
    a_name = models.CharField(max_length=20, verbose_name='院系名称')
    a_profile = models.CharField(max_length=255, verbose_name='院系简介')
    a_establishdate = models.DateField(verbose_name='成立日期')
    a_conceldate = models.DateField(null=True, blank=True, verbose_name='撤销日期')
    a_lastmodifytime = models.DateTimeField(verbose_name='最后修改时间')
    a_modifier_id = models. ForeignKey('User', on_delete=models.CASCADE, verbose_name='academy_modifier',null=True, blank=True)

    class Meta:
        db_table = 'academy'
        verbose_name = '学院'
        verbose_name_plural = '学院'


# 专业表 Major Model
class Major(models.Model):
    m_id = models.IntegerField(primary_key=True, verbose_name='专业ID')
    a_id = models.ForeignKey('Academy', on_delete=models.CASCADE, verbose_name='所属院系ID',null=True, blank=True)
    m_name = models.CharField(max_length=20, verbose_name='专业名称')
    m_profile = models.CharField(max_length=255, verbose_name='专业简介')
    m_trainingplan = models.BinaryField(verbose_name='培养计划')
    m_establishdate = models.DateField(verbose_name='成立日期')
    m_conceldate = models.DateField(null=True, blank=True, verbose_name='撤销日期')
    m_lastmodifytime = models.DateTimeField(verbose_name='最后修改时间')
    m_modifier_id = models. ForeignKey('User', on_delete=models.CASCADE, verbose_name='major_modifier',null=True, blank=True)
    class Meta:
        db_table = 'major'
        verbose_name = '专业'
        verbose_name_plural = '专业'


# 班级表 Class Model
class Class(models.Model):
    c_id = models.IntegerField(primary_key=True, verbose_name='班级ID')
    m_id = models.ForeignKey('Major', on_delete=models.CASCADE, verbose_name='专业ID',null=True, blank=True)
    c_name = models.CharField(max_length=20, verbose_name='班级名称')
    c_profile = models.CharField(max_length=255, verbose_name='班级简介')
    c_enrollmentyear = models.IntegerField(verbose_name='入学年份')
    c_degree = models.CharField(max_length=20, verbose_name='学历层次')
    c_studentnumber = models.IntegerField(verbose_name='学生人数')
    c_lastmodifytime = models.DateTimeField(verbose_name='最后修改时间')
    c_modifier_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='class_modifier',null=True, blank=True)

    class Meta:
        db_table = 'class'
        verbose_name = '班级'
        verbose_name_plural = '班级'


# 实习活动表 IpActivity Model
class IpActivity(models.Model):
    act_id = models.IntegerField(primary_key=True, verbose_name='实习活动ID')
    act_name = models.CharField(max_length=255, verbose_name='实习活动名称')
    act_description = models.CharField(max_length=255, verbose_name='实习活动描述')
    act_begindate = models.DateField(verbose_name='实习开始日期')
    act_enddate = models.DateField(verbose_name='实习结束日期')
    act_status = models.IntegerField(verbose_name='是否结束')

    class Meta:
        db_table = 'ip_activity'
        verbose_name = '实习活动'
        verbose_name_plural = '实习活动'


# 实习活动与班级对应表 IpActivityClass Model
class IpActivityClass(models.Model):
    act_id = models.ForeignKey('IpActivity', on_delete=models.CASCADE, verbose_name='实习活动ID')
    c_id = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name='班级ID')

    class Meta:
        db_table = 'ip_activity_class'
        verbose_name = '实习活动班级对应表'
        verbose_name_plural = '实习活动班级对应表'
        unique_together = ('act_id', 'c_id')  # 保证同一班级与同一实习活动的组合唯一

    def __str__(self):
        return f'{self.act_id.act_name} - {self.c_id.name}'


# 实习岗位表 IpJob Model
class IpJob(models.Model):
    j_id = models.IntegerField(primary_key=True, verbose_name='岗位ID')
    act_id = models.ForeignKey('IpActivity', on_delete=models.CASCADE, verbose_name='实习活动ID',null=True, blank=True)
    cot_id = models.ForeignKey('CompanyTeacher', on_delete=models.CASCADE, verbose_name='企业导师ID',null=True, blank=True)
    j_name = models.CharField(max_length=20, verbose_name='岗位名称')
    j_description = models.CharField(max_length=255, verbose_name='岗位描述')
    j_salary = models.FloatField(verbose_name='实习工资')
    j_type = models.CharField(max_length=45, verbose_name='岗位类型')
    j_begindate = models.DateField(verbose_name='开始时间')
    j_enddate = models.DateField(verbose_name='结束时间')
    j_count = models.IntegerField(verbose_name='人数限制')

    class Meta:
        db_table = 'ip_job'
        verbose_name = '实习岗位'
        verbose_name_plural = '实习岗位'


# 实习申请表 IpApplication Model
class IpApplication(models.Model):
    s_id = models.ForeignKey('Student',on_delete=models.CASCADE,verbose_name='学生ID',null=True, blank=True)
    j_id = models.ForeignKey('IpJob',on_delete=models.CASCADE,verbose_name='实习岗位ID',null=True, blank=True)
    appl_resume = models.BinaryField(verbose_name='简历')
    appl_choice = models.IntegerField(verbose_name='志愿编号')
    appl_status = models.IntegerField(verbose_name='通过状态')

    class Meta:
        db_table = 'ip_application'
        unique_together = ('s_id', 'j_id')
        verbose_name = '实习申请'
        verbose_name_plural = '实习申请'


# 实习周报表 IpWeekly Model
class IpWeekly(models.Model):
    w_id = models.IntegerField(primary_key=True, verbose_name='实习周报ID')
    s_id = models.ForeignKey('Student',on_delete=models.CASCADE,verbose_name='学生ID',null=True, blank=True)
    t_id = models.ForeignKey('Teacher',on_delete=models.CASCADE,verbose_name='校内导师ID',null=True, blank=True)
    cot_id = models.ForeignKey('CompanyTeacher',on_delete=models.CASCADE,verbose_name='企业导师ID',null=True, blank=True)
    w_content = models.BinaryField(verbose_name='实习周报文件')
    w_time = models.CharField(max_length=45, verbose_name='实习周次')
    w_submissiontime = models.DateTimeField(verbose_name='周报提交时间')
    w_t_score = models.IntegerField(null=True, blank=True, verbose_name='校内导师给分')
    w_cot_score = models.IntegerField(null=True, blank=True, verbose_name='企业导师给分')
    t_comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='校内导师评语')
    cot_comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='企业导师评语')
    w_status = models.IntegerField(verbose_name='评阅状态')


# 实习总结表 IpSummary Model
class IpSummary(models.Model):
    sm_id = models.IntegerField(primary_key=True, verbose_name='实习总结ID')
    s_id = models.ForeignKey('Student',on_delete=models.CASCADE,verbose_name='学生ID',null=True, blank=True)
    t_id = models.ForeignKey('Teacher',on_delete=models.CASCADE,verbose_name='校内导师ID',null=True, blank=True)
    cot_id = models.ForeignKey('CompanyTeacher',on_delete=models.CASCADE,verbose_name='企业导师ID',null=True, blank=True)
    sm_submissiontime = models.DateTimeField(verbose_name='提交时间')
    sm_content = models.BinaryField(verbose_name='实习总结文件')
    sm_t_score = models.IntegerField(null=True, blank=True, verbose_name='校内导师给分')
    sm_cot_score = models.IntegerField(null=True, blank=True, verbose_name='企业导师给分')
    t_comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='校内导师评语')
    cot_comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='企业导师评语')
    sm_status = models.IntegerField(verbose_name='评阅状态')

    class Meta:
        db_table = 'ip_summary'
        verbose_name = '实习总结'
        verbose_name_plural = '实习总结'


# 公告表 Announcement Model
class Announcement(models.Model):
    an_id = models.IntegerField(primary_key=True, verbose_name='公告ID')
    an_publisher_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='发布人ID',null=True, blank=True)
    an_title = models.CharField(max_length=200, verbose_name='公告标题')
    an_content = models.TextField(verbose_name='公告内容')
    an_topddl = models.DateField(verbose_name='置顶截止时间')
    an_validityddl = models.DateField(verbose_name='有效期截止日期')
    an_releasetime = models.DateTimeField(verbose_name='发布时间')
    an_viewcount = models.IntegerField(verbose_name='浏览量')

    class Meta:
        db_table = 'announcement'
        verbose_name = '公告'
        verbose_name_plural = '公告'

