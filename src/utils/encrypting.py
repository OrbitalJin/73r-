def inverse(s : str)-> str: 
    return "".join([s[len(s)-1-x] for x in range(len(s))])

def shift(s : str, offset: int = 2)->str:
    return "".join([chr(97 +(ord(x)-97+offset)%26) for x in s if 97<=ord(x)<=122])

def hexadecimal(s : str)->str:
    return "".join([format(ord(x),"x") for x in s])



# print(hexadecimal("abcdefghijklmnopqrstuvwxyz"))
print(hexadecimal("a a"))
print(hex(ord("a")))
