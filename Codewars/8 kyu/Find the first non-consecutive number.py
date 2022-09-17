def first_non_consecutive(arr):
    
    for number in arr[1:]:
        
        if arr[0]+1 != number:
            
            return number
        
        else:
            
            arr.pop(0)