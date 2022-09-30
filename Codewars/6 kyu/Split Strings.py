def solution(s):
    
    lista_s, resultado = list(s), []

    if len(s) % 2 == 0:
    
        for salto in range(0,len(lista_s)+2,2):
            
            resultado.append(''.join(item for item in lista_s[salto-2:salto]))
        
    else:
        
        lista_s.append('_')
        
        for salto in range(0,len(lista_s)+2,2):
            
            resultado.append(''.join(item for item in lista_s[salto-2:salto]))
                
    return resultado[1:]
