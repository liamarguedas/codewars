def increment_string(strng):
    
    lista_numbers = []
    
    if strng == "":
        
        return '1'
    
    else:
    
        if strng[-1].isdigit():

            for x in reversed(strng):

                if x.isdigit():

                    lista_numbers.append(x)

                else:

                    break

            numbers_to_sum = ''.join(lista_numbers[::-1])

            numbers_plus_one = str(int(numbers_to_sum)+1)

            list_without_first_numbers = strng[:-(len(lista_numbers))]

            return list_without_first_numbers+numbers_plus_one.zfill(len(lista_numbers))

        else:

            strng_list = list(strng)

            strng_list.append('1')

            return ''.join(strng_list)