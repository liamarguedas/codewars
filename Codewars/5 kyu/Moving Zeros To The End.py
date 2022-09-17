def move_zeros(lst):
    
    for i in lst:
        
        if i == 0:
            
            lst.pop(lst.index(i))
            
            lst.append(0)
            
    return lst