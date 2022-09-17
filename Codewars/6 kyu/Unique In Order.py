def unique_in_order(iterable):
    
    anterior = None
    
    returned_list=[]
    
    for element in iterable:
        
        if element != anterior:
            
            returned_list.append(element)
            
            anterior = element
            
    return returned_list