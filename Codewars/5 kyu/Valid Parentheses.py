def valid_parentheses(string):
    
    lista = []
    
    for caracter in string:
        
        if caracter == '(':
            
            lista.append(caracter)
        
        elif caracter == ')':
            
            try:
            
                lista.pop()
                
            except:
                
                return False    
            
    return len(lista) == 0