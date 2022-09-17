def narcissistic(value):
    
    str_value = str(value)
    
    number_check=[]
    
    for i in str_value:
        
        number_check.append(int(i))
    
    lista_suma=[]
    
    for number in number_check:
        
        raised = number ** len(number_check)
        
        lista_suma.append(raised)
        
    if sum(lista_suma) == value:
        
        return True
    
    else:
        
        return False