from challenge.src import *


def start(index:int,*args)->str:
    """Start function

    Args:
        index (int): The index of the challenge

    Returns:
        str : The info while starting the challenge
    """
    
    
    if index ==6: # Challenge 6
        
        res = ch6(args[0])
        
        if args[0]==None:
            return "missing url"
        elif res==True:
            return "Website content doesn't contain the word"
        elif res==False:
            return "Your website pass the test , I have already send you the flag"
        else:
            return str(res)
        
    if index==8:  # Challenge 8
        
        res = ch8(args[0])
        
        if args[0]==None:
            return "missing url"
        
        else:
            return res
    
        
        
        
        
    if index==None:
        
        return "missing index value"