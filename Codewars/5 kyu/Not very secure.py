def alphanumeric(password):
    
    if password == '':
        
        return False
    
    num_list = []
    letter_list = []
    nonaccepted = []
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     
    for letter in password:
        
        if letter.lower() not in alphabet and letter.lower() not in numbers:
            
            nonaccepted.append(letter)
        
        else:

            if letter in numbers:

                num_list.append(letter)

            elif letter.isalpha() == True:

                letter_list.append(letter)

    if len(nonaccepted) != 0:
        
        return False
    
    elif len(letter_list) != 0:
        
        return True
    
    elif len(letter_list) != 0 and len(num_list) != 0:
        
        return True