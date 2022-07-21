import mysql.connector as conn

mydb = conn.connect(host  = "Localhost" , user = "root" , passwd = "Ram@12345")

cursor = mydb.cursor()
cursor.execute("insert into ram.hanuman values (15555, 'akshay patel', 'akki9695@gmail.com', 100)")
mydb.commit()
cursor.execute("select  * from ram.hanuman")

for i in cursor.fetchall():
    print(i)