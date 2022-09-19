def find_missing_letter(chars):
    
    if chars[0] == chars[0].upper():
        
        alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        
        lista_verficar = alfabet[alfabet.index(chars[0]):alfabet.index(chars[-1])]
        
        for letra in lista_verficar:
            
            if letra not in chars:
                
                return letra
                
        return alfabet[alfabet.index(chars[-1])+1]
            
    else:
        
        alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        lista_verficar = alfabet[alfabet.index(chars[0]):alfabet.index(chars[-1])]
        
        for letra in lista_verficar:
            
            if letra not in chars:
                
                return letra
                
        return alfabet[alfabet.index(chars[-1])+1]