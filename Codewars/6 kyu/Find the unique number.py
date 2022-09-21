from collections import Counter

def find_uniq(arr):
    
    Unique_counter = Counter(arr)
    
    for number in Unique_counter:
        
        if Unique_counter[number] <= 1:
            
            return number
    

