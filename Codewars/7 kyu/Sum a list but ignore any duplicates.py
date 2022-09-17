from collections import Counter

def sum_no_duplicates(l):
    
    return_list = []
    
    Cantidad = Counter(l)
    
    for numero in l:
        
        if Cantidad[numero] == 1:
            
            return_list.append(numero)
            
    return sum(return_list)