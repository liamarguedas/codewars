from collections import Counter

def first_non_repeating_letter(string):
    
    if string == ' ':
        
        return ' '
    
    else:
    
        count = Counter(string.lower())
        
        for item in string:
            
            if count[item.lower()] == 1:
            
                return item
                
        return ''     