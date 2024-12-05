# Internship-Management-System

数据库课程设计

## django项目环境搭建：

1. 使用mysql创建数据库- “database”
2. 创建虚拟环境

* 方法一：使用命令行在backend\InternshipManagement_sys目录下创建虚拟环境
* 方法二：使用pycharm打开backend\InternshipManagement_sys项目，并在设置中配置解释器“生成新的解释器”（配置虚拟环境）

3. 安装所需要的包。在backend\InternshipManagement_sys目录下的终端中输入命令：pip install -r requirements.txt
4. 生成数据库迁移文件。继续在当前目录下的终端里输入：python manage.py makemigrations 和 python manage.py
5. 搭建完成，输入 py manage.py runserver运行后端代码

