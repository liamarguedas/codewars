def create_phone_number(n):

    country_code = ''.join([str(elem) for elem in n[0:3]])
    
    first_three = ''.join([str(elem) for elem in n[3:6]])
    
    number = ''.join([str(elem) for elem in n[6:]])
    
    return f"({country_code}) {first_three}-{number}"