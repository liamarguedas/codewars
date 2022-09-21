
import itertools

def gta(limit, *args): 
    
    # Lista para para luego sacar el limit.
    lista = []
    
    # Separar numeros de *args en diferentes listas.
    args_list = [number for number in args]
    
    # Calcular Len de todos los números de args para hacer iter en ellos.
    args_len = [len(str(number)) for number in args]
    
    # Crear funcion para Iter por todos los numeros de los numeros de args y agregarlos a "lista" quitando duplicados.
    for n in range(sum(args_len)):
    
        for number in args_list:
            
            if len(str(number)) != 0:
                
                if int(str(number)[0]) not in lista:
                
                    lista.append(int(str(number)[0]))
                        
                    number_str = str(number)[1:]
                        
                    args_list[args_list.index(number)] = number_str
                    
                else:
                    
                    number_str = str(number)[1:]
                        
                    args_list[args_list.index(number)] = number_str
                    
    # Quitar los números de la lista según el limitador
    limited_list = lista[:limit]
    
    # Crear lista para sumar el total
    list_to_sum = []

    # Crear algorithmo para encontrar todas las permutaciones de n+n hasta n+n...limit!
    for item in range(1,len(limited_list)+1):
        
        permutaciones = itertools.permutations(limited_list,item)
        
        # Iter en todas las permutaciones y adicionar la suma de la permutación en list_to_sum.
        for item in permutaciones:
            
            resultado = sum(item)
            
            list_to_sum.append(resultado)
            
    # Return suma de todas las sumas de todas las permutaciones de 1 a limit!
    gta_value = sum(list_to_sum)
    
    return gta_value