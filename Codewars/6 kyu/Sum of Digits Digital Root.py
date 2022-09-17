def digital_root(n):
    
    lista_inicio=[]
    
    for i in str(n):

            lista_inicio.append(int(i))
            
    resultado = sum(lista_inicio)

    while resultado>=10:
        
        segundo_resultado=[]
    
        for i in str(resultado):

            segundo_resultado.append(int(i))

        resultado = sum(segundo_resultado)
        
    return resultado