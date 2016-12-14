import MySQLdb
import os
import ConfigParser


os.chdir("../resource")
config = ConfigParser.ConfigParser()
config.readfp(open("config.ini", "rb"))
ip = config.get("global", "ip")
port = config.get("global", "port")
user = config.get("global", "user")
password = config.get("global", "password")
database = config.get("global", "database")

# print(ip+" "+port+" "+user+" "+password+" "+database)

#######################################################################
conn = MySQLdb.Connect(host=ip,port=int(port), user=user,passwd=password,db=database)
cur  = conn.cursor()
 
cur.execute('select * from testmodel_tag')
print(cur.fetchall())
 
print("ok")
 
cur.close()
conn.close()


