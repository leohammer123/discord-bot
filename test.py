import mysql.connector
from mysql.connector import Error
import time
name = open('log').read().split('\n')
try:
    connection = mysql.connector.connect(
            host='localhost',          
            database='discord_data', 
            user='root',   
            )  

    for r in name:
        request_str =f"INSERT INTO {chr(96)}challenge_solved{chr(96)} ({chr(96)}challenge1{chr(96)}, {chr(96)}challenge2{chr(96)}, {chr(96)}challenge3{chr(96)}, {chr(96)}challenge4{chr(96)}, {chr(96)}challenge5{chr(96)}, {chr(96)}challenge6{chr(96)}, {chr(96)}challenge7{chr(96)}, {chr(96)}challenge8{chr(96)}, {chr(96)}challenge9{chr(96)}, {chr(96)}username{chr(96)}) VALUES ('0', '0', '0', '0', '0', '0', '0', '0', '0', '{r.replace(chr(10),'')}');"
        if connection.is_connected():

            cursor = connection.cursor()
            cursor.execute("update challenge_solved set challenge1=1 where username ='e04qqq#8126'")
            records = cursor.fetchall()
            print(records)
            time.sleep(2)
            cursor.execute("select * from challenge_solved where username ='e04qqq#8126'")
            records = cursor.fetchall()
            print(records)

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")