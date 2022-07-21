import mysql.connector as conn
mydb = conn.connect(host = "localhost" , user = "root", passwd = "Ram@12345")

cursor = mydb.cursor()
#cursor.execute("create database lala")
#a = "create table lala.lala1 (empid int (10) ,empname varchar (100) , empsalry int(10))"
#cursor.execute(a)

cursor.execute("insert into lala.lala1 values (1544167, 'mama', 100000)")
mydb.commit()

cursor.fetchall()