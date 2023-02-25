import re

#Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and 
#returning a string containing the Roman Numeral representation of that integer.

def solution(n):
    roman_nb = ''
    # create a dict to store romain numbers
    roman_nbs = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
        }
    
    temp_nb = n
    for roman_symbol, value in roman_nbs.items():
        #print(divmod(temp_nb, value))
        whole_part = divmod(temp_nb, value)[0]
        if whole_part > 0:
            #print(whole_part)
            #if whole_part := divmod(temp_nb, value)[0] == 0:
                #continue
            #print(whole_part)
            roman_nb += roman_symbol * whole_part
            temp_nb -= value * whole_part
            #print(temp_nb)
    
    pattern_I = r'IIII'
    pattern_I = r'V'
    return roman_nb


while True:
    value = input('Enter an Integer [q to quit]: ')
    if type(value) != 'Int':
        break
    print(f'Roman number is: {solution(int(value))}')





