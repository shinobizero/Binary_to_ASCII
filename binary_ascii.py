# -*- coding: utf-8 -*-

print('Binary To ASCII Converter')
binary_input = '0100110001101111011100100110010101101101001000000110100101110000011100110111010101101101'
#binary_input = '01001100 01101111 01110010 01100101 01101101 00100000 01101001 01110000 01110011 01110101 01101101'

if ' ' in binary_input:
    binary_sequence = binary_input.replace(' ','')
else:
    binary_sequence = binary_input
print('Binary sequence:', " ".join([binary_sequence[i:i+8] for i in range(0, len(binary_sequence), 8)]))

#Separate Binary Sequence to 8 bits
#If Already 8 bits skip
binary_string = ''
binary_character_count = 0
binary_list = []
for bit in binary_sequence:
    binary_character_count += 1
    if binary_character_count % 8 == 0:
        binary_string = binary_string + bit
        binary_list.append(binary_string)
        binary_string = ''
    else:
        binary_string = binary_string + bit

decimal_list = []
for sequence in binary_list:
    conversion_list = []
    reverse_binary_seq = sequence[::-1]
    conversion_list.append(reverse_binary_seq)
    for reverse_sequence in conversion_list:
        conversion = ''
        conversion = conversion + reverse_sequence
        decimal = 0    
        count = 0
        for digit in conversion:
            count += 1
            pwr = count - 1
            digit = int(digit)
            if digit == 1:
                decimal += 2**pwr      
        decimal_list.append(decimal)

ascii_string = ''
for decimal_number in decimal_list:
    ascii_string = ascii_string + chr(decimal_number)
print('Converts to:', ascii_string)