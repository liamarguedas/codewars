from collections import Counter

def permute_a_palindrome(input): 
    
    cantidad = Counter(input) 
  
    return False if len(input) != 0 and len(input) != 2 and sum([(cantidad[item]%2) for item in cantidad]) >= 2 else True 