-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: sims
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `academy`
--

DROP TABLE IF EXISTS `academy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `academy` (
  `a_id` int NOT NULL COMMENT '院系Id',
  `a_name` varchar(20) COLLATE utf8mb3_bin NOT NULL COMMENT '院系名称',
  `a_profile` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '院系简介',
  `a_dean` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '院长',
  `a_establishdate` date NOT NULL COMMENT '成立日期',
  `a_conceldate` date DEFAULT NULL COMMENT '撤销日期',
  `a_lastmodifytime` datetime(2) NOT NULL COMMENT '最后修改时间',
  `a_modifier` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '修改人',
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='学院';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academy`
--

LOCK TABLES `academy` WRITE;
/*!40000 ALTER TABLE `academy` DISABLE KEYS */;
/*!40000 ALTER TABLE `academy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `announcement`
--

DROP TABLE IF EXISTS `announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `announcement` (
  `an_id` int NOT NULL COMMENT '公告id',
  `an_publisherid` int NOT NULL COMMENT '发布人id',
  `an_title` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '公告标题',
  `an_content` mediumtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '公告内容',
  `an_topddl` date NOT NULL COMMENT '置顶截止时间',
  `an_validityddl` date NOT NULL COMMENT '有效期截止日期',
  `an_releasetime` datetime(2) NOT NULL COMMENT '发布时间',
  `an_viewcount` int NOT NULL COMMENT '浏览量',
  PRIMARY KEY (`an_id`),
  KEY `announcement_ibfk_1` (`an_publisherid`),
  CONSTRAINT `announcement_ibfk_1` FOREIGN KEY (`an_publisherid`) REFERENCES `user` (`u_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='公告';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcement`
--

LOCK TABLES `announcement` WRITE;
/*!40000 ALTER TABLE `announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `c_id` int NOT NULL COMMENT '班级id',
  `m_id` int NOT NULL COMMENT '专业ID',
  `t_id` int NOT NULL COMMENT '班主任Id',
  `act_id` int DEFAULT NULL,
  `c_name` varchar(20) NOT NULL COMMENT '班级名称',
  `c_profile` varchar(255) NOT NULL COMMENT '班级简介',
  `c_enrollmentyear` year NOT NULL COMMENT '入学年份',
  `c_degree` varchar(20) NOT NULL COMMENT '学历层次',
  `c_studentnumber` int NOT NULL COMMENT '学生人数',
  `c_lastmodifytime` datetime(2) NOT NULL COMMENT '最后修改时间',
  `c_modifier` varchar(20) NOT NULL COMMENT '修改人',
  PRIMARY KEY (`c_id`),
  KEY `class_ibfk_1` (`m_id`),
  KEY `class_ibfk_2` (`t_id`),
  KEY `act_id` (`act_id`),
  CONSTRAINT `class_ibfk_1` FOREIGN KEY (`m_id`) REFERENCES `major` (`m_id`),
  CONSTRAINT `class_ibfk_2` FOREIGN KEY (`t_id`) REFERENCES `teacher` (`t_id`),
  CONSTRAINT `class_ibfk_3` FOREIGN KEY (`act_id`) REFERENCES `ip_activity` (`act_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='班级';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `co_id` int NOT NULL COMMENT '企业ID',
  `co_name` varchar(20) COLLATE utf8mb3_bin NOT NULL COMMENT '企业名称\\n',
  `co_address` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '企业地址\\n',
  `co_contacts` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '联系人\\n',
  `co_scale` int NOT NULL COMMENT '企业规模',
  PRIMARY KEY (`co_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='企业';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_teacher`
--

DROP TABLE IF EXISTS `company_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_teacher` (
  `cot_id` int NOT NULL COMMENT '企业导师id',
  `co_id` int NOT NULL COMMENT '企业ID',
  `act_id` int DEFAULT NULL COMMENT '管理的实习活动id',
  `cot_name` varchar(20) NOT NULL COMMENT '企业导师名称',
  `cot_title` varchar(45) NOT NULL COMMENT '职称/头衔',
  PRIMARY KEY (`cot_id`),
  KEY `company_teacher_ibfk_1` (`co_id`),
  KEY `company_teacher_ibfk_2` (`act_id`),
  CONSTRAINT `company_teacher_ibfk_1` FOREIGN KEY (`co_id`) REFERENCES `company` (`co_id`),
  CONSTRAINT `company_teacher_ibfk_2` FOREIGN KEY (`act_id`) REFERENCES `ip_activity` (`act_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='企业导师';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_teacher`
--

LOCK TABLES `company_teacher` WRITE;
/*!40000 ALTER TABLE `company_teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_activity`
--

DROP TABLE IF EXISTS `ip_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip_activity` (
  `act_id` int NOT NULL COMMENT '实习活动id',
  `co_id` int NOT NULL COMMENT '企业id',
  `act_name` int NOT NULL COMMENT '实习活动名称',
  `act_description` varchar(255) NOT NULL COMMENT '实习活动描述',
  `act_begindate` date NOT NULL COMMENT '实习开始日期',
  `act_enddate` date NOT NULL COMMENT '实习结束日期',
  PRIMARY KEY (`act_id`),
  KEY `ip_activity_ibfk_1` (`co_id`),
  CONSTRAINT `ip_activity_ibfk_1` FOREIGN KEY (`co_id`) REFERENCES `company` (`co_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='实习活动表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_activity`
--

LOCK TABLES `ip_activity` WRITE;
/*!40000 ALTER TABLE `ip_activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_application`
--

DROP TABLE IF EXISTS `ip_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip_application` (
  `appl_id` int NOT NULL COMMENT '实习申请表id',
  `s_id` int NOT NULL COMMENT '学生id',
  `j_id` int NOT NULL COMMENT '实习岗位id',
  `appl_resume` blob NOT NULL COMMENT '简历pdf',
  `appl_choice` int NOT NULL COMMENT '志愿编号（0不选，1第一志愿，2第二志愿，3第三志愿）',
  `appl_status` int NOT NULL COMMENT '申请表状态，0未审阅，1已审阅',
  PRIMARY KEY (`appl_id`),
  KEY `ip_application_ibfk_1` (`s_id`),
  KEY `ip_application_ibfk_2` (`j_id`),
  CONSTRAINT `ip_application_ibfk_1` FOREIGN KEY (`s_id`) REFERENCES `student` (`s_id`),
  CONSTRAINT `ip_application_ibfk_2` FOREIGN KEY (`j_id`) REFERENCES `ip_job` (`j_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='实习申请';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_application`
--

LOCK TABLES `ip_application` WRITE;
/*!40000 ALTER TABLE `ip_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_job`
--

DROP TABLE IF EXISTS `ip_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip_job` (
  `j_id` int NOT NULL COMMENT '岗位ID',
  `act_id` int NOT NULL COMMENT '实习活动ID',
  `co_id` int NOT NULL COMMENT '公司ID',
  `j_name` varchar(20) NOT NULL COMMENT '岗位名称',
  `j_description` varchar(255) NOT NULL COMMENT '岗位描述',
  `j_salary` float NOT NULL COMMENT '实习工资',
  `j_type` varchar(45) NOT NULL COMMENT '岗位类型',
  `j_begindate` date NOT NULL COMMENT '开始时间',
  `j_enddate` date NOT NULL COMMENT '结束时间',
  `j_count` int NOT NULL COMMENT '人数限制',
  PRIMARY KEY (`j_id`),
  KEY `ip_job_ibfk_1` (`act_id`),
  KEY `ip_job_ibfk_2` (`co_id`),
  CONSTRAINT `ip_job_ibfk_1` FOREIGN KEY (`act_id`) REFERENCES `ip_activity` (`act_id`),
  CONSTRAINT `ip_job_ibfk_2` FOREIGN KEY (`co_id`) REFERENCES `company` (`co_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='实习岗位';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_job`
--

LOCK TABLES `ip_job` WRITE;
/*!40000 ALTER TABLE `ip_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_summary`
--

DROP TABLE IF EXISTS `ip_summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip_summary` (
  `sm_id` int NOT NULL COMMENT '实习总结id',
  `s_id` int NOT NULL COMMENT '学生ID',
  `t_id` int NOT NULL COMMENT '校内导师id',
  `cot_id` int NOT NULL COMMENT '企业导师id',
  `sm_submissiontime` datetime(2) NOT NULL COMMENT '提交时间',
  `sm_content` blob NOT NULL COMMENT '实习总结pdf',
  `sm_t_score` int DEFAULT NULL COMMENT '校内导师给分',
  `sm_ct_score` int DEFAULT NULL COMMENT '企业导师给分',
  `t_comment` varchar(255) DEFAULT NULL COMMENT '校内导师评语',
  `cot_comment` varchar(255) DEFAULT NULL COMMENT '企业导师评语',
  `sm_status` int NOT NULL COMMENT '状态',
  PRIMARY KEY (`sm_id`),
  KEY `ip_summary_ibfk_1` (`s_id`),
  KEY `cot_id` (`cot_id`),
  KEY `t_id` (`t_id`),
  CONSTRAINT `ip_summary_ibfk_1` FOREIGN KEY (`s_id`) REFERENCES `student` (`s_id`),
  CONSTRAINT `ip_summary_ibfk_2` FOREIGN KEY (`cot_id`) REFERENCES `company_teacher` (`cot_id`),
  CONSTRAINT `ip_summary_ibfk_3` FOREIGN KEY (`t_id`) REFERENCES `teacher` (`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='实习总结';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_summary`
--

LOCK TABLES `ip_summary` WRITE;
/*!40000 ALTER TABLE `ip_summary` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_weekly`
--

DROP TABLE IF EXISTS `ip_weekly`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip_weekly` (
  `w_id` int NOT NULL COMMENT '实习周报id',
  `s_id` int NOT NULL COMMENT '学生ID',
  `t_id` int NOT NULL COMMENT '校内导师id',
  `cot_id` int NOT NULL COMMENT '企业导师id',
  `w_content` blob NOT NULL COMMENT '周报pdf',
  `w_time` varchar(45) NOT NULL COMMENT '实习周次（第几次）\\n',
  `w_submissiontime` datetime(2) NOT NULL COMMENT '周报提交时间',
  `w_status` int NOT NULL DEFAULT '0',
  `w_t_score` int DEFAULT NULL COMMENT '校内导师周报评分',
  `w_cot_score` varchar(45) DEFAULT NULL COMMENT '企业导师周报评分',
  `w_t_comment` varchar(255) DEFAULT NULL,
  `w_cot_comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`w_id`),
  KEY `s_id` (`s_id`),
  KEY `t_id` (`t_id`),
  KEY `cot_id` (`cot_id`),
  CONSTRAINT `ip_weekly_ibfk_1` FOREIGN KEY (`s_id`) REFERENCES `student` (`s_id`),
  CONSTRAINT `ip_weekly_ibfk_2` FOREIGN KEY (`t_id`) REFERENCES `teacher` (`t_id`),
  CONSTRAINT `ip_weekly_ibfk_3` FOREIGN KEY (`cot_id`) REFERENCES `company_teacher` (`cot_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='实习周报';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_weekly`
--

LOCK TABLES `ip_weekly` WRITE;
/*!40000 ALTER TABLE `ip_weekly` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_weekly` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major`
--

DROP TABLE IF EXISTS `major`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `major` (
  `m_id` int NOT NULL COMMENT '专业ID',
  `a_id` int NOT NULL COMMENT '所属院系id',
  `m_name` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `m_profile` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '专业简介',
  `m_trainingplan` blob NOT NULL COMMENT '培养计划pdf',
  `m_establishdate` date NOT NULL COMMENT '成立日期',
  `m_conceldate` date DEFAULT NULL COMMENT '撤销日期',
  `m_lastmodifytime` datetime(2) NOT NULL COMMENT '最后修改时间',
  `m_modifier` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '最后修改人',
  PRIMARY KEY (`m_id`),
  KEY `a_id` (`a_id`),
  CONSTRAINT `major_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `academy` (`a_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='专业';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major`
--

LOCK TABLES `major` WRITE;
/*!40000 ALTER TABLE `major` DISABLE KEYS */;
/*!40000 ALTER TABLE `major` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `s_id` int NOT NULL COMMENT '学生ID',
  `c_id` int NOT NULL COMMENT '班级ID',
  `s_name` varchar(20) NOT NULL COMMENT '学生姓名',
  `s_grade` varchar(20) NOT NULL COMMENT '学生年级',
  `s_state` binary(1) NOT NULL COMMENT '实习状态，0为否，1为是',
  PRIMARY KEY (`s_id`),
  KEY `student_ibfk_1` (`c_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `class` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='学生';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `t_id` int NOT NULL COMMENT '老师ID',
  `c_id` int NOT NULL COMMENT '管理班级ID',
  `t_name` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '老师姓名',
  `t_type` int NOT NULL COMMENT '0不是班主任，1是班主任\\n',
  PRIMARY KEY (`t_id`),
  KEY `c_id` (`c_id`),
  CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `class` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='校内导师';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `u_id` int NOT NULL COMMENT '用户ID',
  `u_password` varchar(20) COLLATE utf8mb3_bin NOT NULL DEFAULT '123456' COMMENT '密码',
  `u_type` int NOT NULL COMMENT '用户类型，0为管理员，1为学生，2为班主任，3为企业导师',
  `u_tel` char(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `u_photo` blob,
  `u_status` int NOT NULL DEFAULT '0' COMMENT '激活状态，0为未激活，1为已激活',
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='用户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04 11:23:28
