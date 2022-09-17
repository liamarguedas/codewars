from collections import Counter

def score(dice):
    
    score = 0
    
    cantidad = Counter(dice)
    
    for item in cantidad:
        
        if cantidad[item] == 1:
            
            if item == 5:
                
                score += 50
                
            elif item == 1:
                
                score += 100
        
        elif cantidad[item] <= 3 or cantidad[item] >= 3:
            
            # Si hay más de tres, 1's en la lista    
            if item == 1 and cantidad[item] > 3:
                
                extra_number = cantidad[item] - 3
                
                to_add = 100 * extra_number
                
                score += 1000 + to_add
                
            # Si hay más de tres, 5's en la lista    
            elif item == 5 and cantidad[item] > 3:
                
                extra_number = cantidad[item] - 3
                
                to_add = 50 * extra_number
                
                score += 500 + to_add
                
            # Si hay menos de tres, 1's en la lista                
            elif item == 1 and cantidad[item] < 3:
                
                to_add = cantidad[item] * 100
                
                score += to_add
                
            # Si hay menos de tres, 5's en la lista
            elif item == 5 and cantidad[item] < 3:
                
                to_add = cantidad[item] * 50
                
                score += to_add
            
            # Si hay tres, 1s en la lista    
            elif item == 1 and cantidad[item] == 3:
                
                score += 1000
                
            # Si hay tres 2's en la lista    
            elif item == 2 and cantidad[item] >= 3:
                
                score += 200
                
            # Si hay tres 3's en la lista    
            elif item == 3 and cantidad[item] >= 3:
                
                score += 300
                
            # Si hay tres 4's en la lista
            elif item == 4 and cantidad[item] >= 3:
                
                score += 400
                
            elif item == 5 and cantidad[item] == 3:
                
                score += 500
            
            # Si hay tres 6's en la lista
            if item == 6 and cantidad[item] >= 3:
                
                score += 600
        
        else:
            
            continue
        
    print(score)
    
    
score([2,2,2,1,0])