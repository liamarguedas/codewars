from random import shuffle

def next_bigger(n):
    
    lista = list(str(n))
    
    lista_to_compare = []
    
    # If theres no bigger number than n
    
    if set(str(n)) == {str(n)[0]} or len(str(n)) == 1:
        
        return -1
    
    # If number is smaller than 1000.
                            
    elif len(str(n)) < len(str(10000)):
            
        for number in range(n):
        
            shuffle(lista)
            
            for numero in lista:
                    
                number_appen = "".join(lista)
                    
                if int(number_appen) > n:
                
                    lista_to_compare.append(int(number_appen))
                    
    #If number is bigger than 10000.
        
    else:
    
        last_three_list = lista[-7:]
        
        for number in range(4000):
        
            shuffle(last_three_list)
            
            for numero in last_three_list:
                    
                number_appen = "".join(last_three_list)
                
                if int(number_appen) > int(str(n)[-7:]):
                       
                    lista_to_compare.append(int(str("".join(lista[0:-7]))+str(number_appen)))
    
    if len(lista_to_compare) == 0:
        
        return -1 
    
    else: 
           
        return min(lista_to_compare)