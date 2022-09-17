import numpy as np
from collections import Counter

def valid_solution(board):
    
    if board == ' ':
        
        return False
    
    else:
    
        array = np.array(board)

        for cell in range(9):
            
            for number in array[cell]:

                if number == 0:
                    
                    return False

            # Verificar si valor se repite en linea vertical

            lista_check_vertical = []

            for number in array[:,cell]:

                if number not in lista_check_vertical:

                    lista_check_vertical.append(number)

                else:

                    return False

            # Verificar si valor se repite en linea horizontal

            lista_check_horizontal = []

            for number in array[cell]:

                if number not in lista_check_horizontal:

                    lista_check_horizontal.append(number)

                else:

                    return False

        # Verificar cuadrado de 3x3

        # Verificar primer 3x3, (0,1,2 / 0,1,2)

        lista_verificacion = []

        for cells in range(3):

            for number in array[cells][:3]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar segundo 3x3, (0,1,2 / 3,4,5)
        lista_verificacion = []

        for cells in range(3):

            for number in array[cells][3:6]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

         # Verificar tercer 3x3, (0,1,2 / 6,7,8)
        lista_verificacion = []

        for cells in range(3):

            for number in array[cells][6:9]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar cuarto 3x3, (3,4,5 / 0,1,2)
        lista_verificacion = []

        for cells in range(3,6):

            for number in array[cells][:3]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar quinto 3x3, (3,4,5 / 3,4,5)
        lista_verificacion = []

        for cells in range(3,6):

            for number in array[cells][3:6]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar sexto 3x3, (3,4,5 / 6,7,8)
        lista_verificacion = []

        for cells in range(3,6):

            for number in array[cells][6:9]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar septimo 3x3, (6,7,8 / 0,1,2)
        lista_verificacion = []

        for cells in range(6,9):

            for number in array[cells][:3]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar quinto 3x3, (6,7,8 / 3,4,5)
        lista_verificacion = []

        for cells in range(6,9):

            for number in array[cells][3:6]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False

        # Verificar sexto 3x3, (6,7,8 / 6,7,8)
        lista_verificacion = []

        for cells in range(6,9):

            for number in array[cells][6:9]:

                lista_verificacion.append(number)

                for cantidad in Counter(lista_verificacion).values():

                    if cantidad != 1:

                        return False          

        return True