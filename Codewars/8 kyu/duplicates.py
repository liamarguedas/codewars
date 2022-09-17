from collections import OrderedDict

def distinct(seq):
    
    return list(OrderedDict.fromkeys(seq))
    
 
   
distinct([1, 1, 1, 2, 3, 4, 5])