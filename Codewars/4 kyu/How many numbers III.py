from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    
    combinaciones = combinations_with_replacement(list(range(1, 10)), digs)
    
    lista_final = [''.join(str (x) for x in list(comb)) for comb in combinaciones if sum(comb) == sum_dig]
    
    if len(lista_final) == 0:
        
        return []
    
    return [len(lista_final), int(lista_final[0]), int(lista_final[-1])]
