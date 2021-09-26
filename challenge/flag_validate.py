import hashlib
import mysql.connector
from mysql.connector import Error

def write_record(name,challenge):
  try:
      connection = mysql.connector.connect(
              host='localhost',          
              database='discord_data', 
              user='root',   
              )  
      if connection.is_connected():
        cursor = connection.cursor()
        if name == 'leo123#9956':
          cursor.execute("update challenge_solved set challenge{}=0 where username ='leo123#9956\r\n'".format(challenge))
          records = cursor.fetchall()
          cursor.execute("select * from challenge_solved where username ='leo123#9956\r\n'")
          records = cursor.fetchall()
          print(records)
        else:
          cursor.execute("update challenge_solved set challenge{}=1 where username ='{}'".format(challenge,name))
          cursor.execute("select * from challenge_solved where username ='{}'".format(name))
          records = cursor.fetchall()
          print(records)


  except Error as e:
      print("資料庫連接失敗：", e)

  finally:
      if (connection.is_connected()):
          cursor.close()
          connection.close()
          print("資料庫連線已關閉")
    



def flag_check(flag,name): 
    with open('flaglist.txt','r') as flah:
      r = flah.read().split('\n')
      solve = 0
      line = 0
      for n in r:
        if n.split(':')[1] == hashlib.sha256(flag.encode()).hexdigest():
          solve =1
          write_record(name,line+1)
          continue
        else:
          line+=1
    return solve