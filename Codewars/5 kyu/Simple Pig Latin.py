def pig_it(text):
    
    lista_text = text.split(' ')
    
    lista_reversed = []
    
    lista_returned = []
    
    for word in lista_text:
        
        word = word + ''.join(word[0])
        
        
        lista_reversed.append(word[1:])
      
    for word in lista_reversed:
        
        if word.isalpha() == False:
            
            lista_returned.append(word)
        
        else:
            
            ay = 'ay'
            
            word = word + "".join(ay)  
            
            lista_returned.append(word)
    
    return ' '.join(lista_returned)