from collections import Counter

def scramble(s1, s2):
   
   find,string,find_qty,string_qty = s1,s2,Counter(find),Counter(string)
   
   # Eliminar letras que no harian match entre match/string
   for letra in find:
      
      if letra not in string:
         
         find = find.replace(letra,'')
         
   # Verificar que la cantidad de letras de find hace match con string
   for letra1 in sorted(find_qty.keys()):
   
      for letra2 in sorted(string_qty.keys()):
   
         if letra1 == letra2 and find_qty[letra1] > string_qty[letra2]:
               
            find = find.replace(letra1,"",find_qty[letra1]-string_qty[letra2])
   return sorted(find) == sorted(string)