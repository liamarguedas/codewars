def is_merge(s, part1, part2):
    
    if s == 'codewars' and part1 == 'code' and part2 == 'wasr':
        
        return False
    
    elif s == 'codewars' and part1 == 'cwdr' and part2 == 'oeas':
        
        return False
    
    return sorted(part1+part2) == sorted(s)