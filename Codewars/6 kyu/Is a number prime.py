from math import sqrt

def definir_rango(inicio, final, paso):
    
    while inicio < final:
        
        yield inicio
        
        inicio += paso
        
        
def is_prime(num):
    
    if num == 2:
        
        return True
    
    elif num < 2 or num % 2 == 0:
        
        return False
    
    return all(num % item for item in definir_rango(3, int(sqrt(num)) + 1, 2))