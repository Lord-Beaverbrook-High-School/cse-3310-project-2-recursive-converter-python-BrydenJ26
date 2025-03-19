def hex_to_dec(base16):
    """
    Input: Takes in a string of hexadecimal digits ("1C2A3")
    Process: Checks to see if the string is empty and if so gives a 0. But if not takes everything to the left of index 1,
    excluding itself, and if it's a letter than it takes it corresponding number (i.e. A=10, B=11, etc.) multiplies it by
    16 to the power of the length of the string minus 1, adding it recursively to the rest of the string. If it's not a
    letter than it takes the number multiplies it by 16 to the power of the length of the string minus 1, adding it recursively
    to the rest of the string
    Output: The decimal representation of the hexadecimal digits (115363)
    """
    if base16 == '':
        return 0
    elif base16[:1] == 'A':
        return (10 * (16 ** (len(base16) - 1))) + hex_to_dec(base16[1:])
    elif base16[:1] == 'B':
        return (11 * (16 ** (len(base16) - 1))) + hex_to_dec(base16[1:])
    elif base16[:1] == 'C':
        return (12 * (16 ** (len(base16) - 1))) + hex_to_dec(base16[1:])
    elif base16[:1] == 'D':
        return (13 * (16 ** (len(base16) - 1))) + hex_to_dec(base16[1:])
    elif base16[:1] == 'E':
        return (14 * (16 ** (len(base16) - 1))) + hex_to_dec(base16[1:])
    elif base16[:1] == 'F':
        return (15 * (16 ** (len(base16) - 1))) + hex_to_dec(base16[1:])
    else:
        return int(base16[0]) * (16 ** (len(base16) - 1)) + hex_to_dec(base16[1:])

def dec_to_hex(base10):
    """
    Input: Takes in an integer (45678)
    Process: Sees if the number is equal to 0 and if so gives an empty string in return. But if it's not 0 than it divides
    the integer by 16 and keeps the remainder. If the remainder is >= 10 than the number is substituted with its corresponding
    hexadecimal letter (i.e. 10=A, 11=B, etc.)
    Output: The hexadecimal representation of the integer (B26E)
    """
    if base10 == 0:
        return ''
    elif (base10 % 16) < 10:
        return dec_to_hex(base10 // 16) + str(base10 % 16)
    elif (base10 % 16) == 10:
        return dec_to_hex(base10 // 16) + 'A'
    elif (base10 % 16) == 11:
        return dec_to_hex(base10 // 16) + 'B'
    elif (base10 % 16) == 12:
        return dec_to_hex(base10 // 16) + 'C'
    elif (base10 % 16) == 13:
        return dec_to_hex(base10 // 16) + 'D'
    elif (base10 % 16) == 14:
        return dec_to_hex(base10 // 16) + 'E'
    elif (base10 % 16) == 15:
        return dec_to_hex(base10 // 16) + 'F'

def bin_to_dec(base2):
    """
    Input: Takes in a string of binary numbers ("101010101")
    Process: Checks to see if the string is empty and if so it gives 0. But if not it takes the number, converts it to a
    string, and takes the number at index 0 and multiplies it by 2 to the power of the strings length minus 1 then adds
    this to the recursion of the number at index 1 and above
    Output: The integer representation of the binary number (341)
    """
    if base2 == '':
        return 0
    else:
        return (int(base2[0])) * (2 ** (len(base2) - 1)) + bin_to_dec(base2[1:])

def dec_to_bin(base10):
    """
    Input: Takes in an integer (456)
    Process: Checks to see if the number is equal to zero and if so return an empty string, but if not recursively divide
    the number by 2 and return the rounded down number plus the remainder of the number when divided by 2
    Output: The binary representation of the integer (111001000)
    """
    if base10 == 0:
        return ''
    else:
        return dec_to_bin(base10 // 2) + str(base10 % 2)


print(hex_to_dec("1C2A3"))
print(dec_to_hex(45678))
print(bin_to_dec("101010101"))
print(dec_to_bin(456))
