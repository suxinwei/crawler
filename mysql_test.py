import pymysql

db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()
# dbsql = 'CREATE DATABASE spiders DEFAULT CHARACTER SET utf8'  // 创建数据库
dbsql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'  # 创建表
cursor.execute(dbsql)
db.close()
