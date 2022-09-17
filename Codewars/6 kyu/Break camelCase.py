from collections import Counter

def solution(s):
    
    lista = [letra for letra in s]
    
    index = 0
    
    for mayuscula in s:

        if mayuscula.upper() == mayuscula:
            
            if " " in lista:
                
                spaces = Counter(lista)
                
                lista.insert(index + spaces[' ']," ")
                
                index += 1
                
            else:
            
                lista.insert(index," ")
            
                index += 1

        else:
    
            index += 1
            
    return "".join(lista)