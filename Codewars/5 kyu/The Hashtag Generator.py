def generate_hashtag(s):
    
    lista = []
    
    if len(s)>=139:
        
        return False
    
    elif s == '':
        
        return False
    
    else:
        s.split(' ')
        
        for i in s.split(' '):
            
            lista.append(i.capitalize())
            
        return f'#{"".join(lista)}'