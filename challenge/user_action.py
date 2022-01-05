from operator import itemgetter
import json
from challenge.db import *

def flag_validate(flag:str,id:int):
    """ flag_valiate : validate the flag

    Args:
        flag (str): flag string
        id (int): user discord id

    Returns:
        result(str): result after validate
    """
    
    
    solve_level = []
    flaglist = open("challenge\\flaglist.txt").read().splitlines()
    
    try:
        record = bin(search(id)[0][2])[2:].zfill(24)
    
    except IndexError:
        return "User not found \nPlease creat your account first , Use '#create'"
    
    """
    Search(id) return all info about the user, take the second parameter and transfer it to binary.
    
    Ex.
    
    100000000000000000000000 (binary)
    
    8388608 (decimal)
    
    Only solve first challenge
    
    110000000000000000000000 (binary)
    
    12582912(decimal)
    
    Solve fisrt and second challenge

    """

    for r in record:
        if r =="0":
            solve_level.append(0)
        else:
            solve_level.append(1)   

    
    index = 0
    
    for k in flaglist:
        
        if k == flag:
            
            if not(solve_level[index]):
                
                solve_level[index]  = solve_level[index]+1
                level = int(''.join(str(j) for j in solve_level),2)
                index += 1
                n = json.loads(open("challenge\data\challenge_info.json",'r',encoding="utf-8").read())[index-1]
                insert(id,n["score"],level)

                return f"Congrat you solve \"{n['title']}\"\n Now your score is **{str(search(id)[0][1])}**"
                
            else:
                return "You have solved this challenge"
        else:
            index += 1
            
            
        if index == len(flaglist):
            return "Flag isn't correct"
    
    
def create(id:int):
    
    text = creat_user(id) 
    return text
        

def score(id:int):
    return f"Your score : {str(search(id)[0][1])}" 