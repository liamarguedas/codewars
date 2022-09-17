def solution(number):
    
    list_to_sum = []

    lista_numeros = list(range(1,number))
    
    for number in lista_numeros:
        
        if number % 3 == 0 or number % 5 == 0:
            
            list_to_sum.append(number)
            
    return sum(list_to_sum)