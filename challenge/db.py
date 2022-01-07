import sqlite3

db = sqlite3.connect('challenge\data\score.db')
cursor = db.cursor()

def creat_user(id:int):

    if search(id):
        return "This discord id already have an account"
    
    
    query = f"INSERT INTO SCOREBOARD (SCORE,DC_ID,LEVEL) VALUES('{0}','{id}','{0}')"
    cursor.execute(query)
    db.commit()
    return "User Create Succeed"

#Create db query
def creat_db():
    
    query = """CREATE TABLE SCOREBOARD
    (DC_ID INT NOT NULL,
    SCORE INT NOT NULL,
    LEVEL INT NOT NULL);"""

    cursor.execute(query)
    db.commit()
    return "Datebase created"
    
def search(id:int):
    
    return cursor.execute(f"SELECT * FROM SCOREBOARD WHERE DC_ID='{id}'").fetchall()

    
def insert(id:int,score:int,level:int):
    
        query = f"SELECT * FROM SCOREBOARD WHERE DC_ID='{id}';"
        res = cursor.execute(query).fetchall()
        
        if not(res):
            return "User not found"

        query = f"UPDATE SCOREBOARD SET SCORE=SCORE+'{score}', LEVEL='{level}' WHERE DC_ID='{id}'"
        cursor.execute(query)
        db.commit()
        
        return "Update succeed"

def test():
    

    query = f"SELECT * FROM SCOREBOARD"
    
    return cursor.execute(query).fetchall()
