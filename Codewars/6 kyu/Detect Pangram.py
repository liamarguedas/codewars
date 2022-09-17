def is_pangram(s):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    lenght = len(alphabet)
    
    count=0
    
    for letter in s:
        
        if letter.lower() not in alphabet:
            
            continue
            
        elif letter.lower() in alphabet:
            
            count+=1
            
            alphabet.pop(alphabet.index(letter.lower()))
        
    return count == lenght