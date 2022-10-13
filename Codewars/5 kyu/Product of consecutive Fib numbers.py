def productFib(prod):

    primer_numero,segundo_numero,fibonacci_numero= 0,1,0
    
    while fibonacci_numero < prod:
        
        fibonacci_numero = primer_numero + segundo_numero
        
        primer_numero = segundo_numero
        
        segundo_numero = fibonacci_numero  
        
        if primer_numero * fibonacci_numero <= prod:
            
            if primer_numero * fibonacci_numero == prod:
                        
                return [primer_numero,fibonacci_numero,True]
                
        elif primer_numero * fibonacci_numero > prod:
                
            return [primer_numero,fibonacci_numero,False]
            
    return [0, 1, True]