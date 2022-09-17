from collections import Counter

def sum_no_duplicates(l):
    
    return_list = []
    
    Cantidad = Counter(l)
    
    for numero in l:
        
        if Cantidad[numero] == 1:
            
            return_list.append(numero)
            
    print(sum(return_list))
    
sum_no_duplicates([1, 1, 2, 2, 3])