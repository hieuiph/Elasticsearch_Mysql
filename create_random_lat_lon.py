import MySQLdb as mysql
import random

conn = mysql.connect(host='127.0.0.1',port = 3306, user='root', passwd='', db='hozo')

with conn:
         cursor = conn.cursor()
      
         query = """CREATE TABLE IF NOT EXISTS task_test 
                                 (id int(11) PRIMARY KEY AUTO_INCREMENT,
                                  title varchar(255), 
                                  place varchar(255), 
                                  lat float, 
                                  lon float);"""
         cursor.execute(query)
         titles = ['don nha', 'sua chua do dien', 'IT', 'Boc vac', 'tiep thi', 'Phat to roi','hoc thue' ]
         places = ['Dong Da', 'Hai Ba Trung', 'Truong Chinh', 'Bach Khoa', 'My Dinh','Ba Dinh', 'Long Bien','Thanh Xuan', 'Ha Dong']
         
         for i in range(1,1000001):
             title = random.choice(titles)
             place = random.choice(places)
             #lat = ('%.6f' % (21.345654+random.random()/100))
             #lon = ('%.6f' % (105.804817+random.random()/100))
             lat = random.uniform(20.6546,21.3687)
             lon = random.uniform(105.2600,106.2296)
             sql = "INSERT INTO task_test(title,place,lat,lon) VALUES (%s,%s,%s,%s)"
             cursor.execute(sql,(title,place,lat,lon))
   




