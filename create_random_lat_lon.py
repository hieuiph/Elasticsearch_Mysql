import MySQLdb as mysql
import random

conn = mysql.connect(host='127.0.0.1',port = 3306, user='root', passwd='', db='hozo')

with conn:
         cursor = conn.cursor()
         for i in range(1,10001):
             lat = ('%.6f' % (21.345654+random.random()/100))
             lon = ('%.6f' % (105.804817+random.random()/100))
             sql = "INSERT INTO lat_lon(lat,lon) VALUES (%s,%s)"
             cursor.execute(sql,(lat,lon))
             

