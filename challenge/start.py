from challenge.scr import *

def start(index:int,*args)->str:
    """Start function

    Args:
        index (int): The index of the challenge

    Returns:
        str : The info while starting the challenge
    """
    
    
    if index ==6:
        res = ch6(args[0])
        if args[0]==None:
            return "missing url"

        if res==False:
            return "solve"
        
        elif res==True:
            return "Website content doesn't contain the word"
        else:
            return str(res)
        

    

    