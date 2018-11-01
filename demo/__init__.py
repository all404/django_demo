"""
数据库配置1(先要pip install pymysql)
作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。
"""
from pymysql import install_as_MySQLdb

install_as_MySQLdb()