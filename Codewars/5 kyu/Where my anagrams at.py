def anagrams(word, words):
    
    return_list = []
    
    for palabra in words:
        
        if sorted(palabra) == sorted(word):
            
            return_list.append(palabra)
    
    return return_list