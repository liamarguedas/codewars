def high_and_low(numbers):
    
    numbers = numbers.split(' ')
    
    lista_verificar = [int(number) for number in numbers]
    
    return f"{max(lista_verificar)} {min(lista_verificar)}"