str_to_morse = {"a": ".-", "b" : "-...", "c" : "-.-.",
                "d": "-..", "e": ".", "f": "..-.",
                "g": "--.", "h": "....", "i": "..",
                "j": ".---", "k": "-.-", "l": ".-..", 
                "m": "--", "n": "-.", "o": "---",
                "p": ".--.", "q": "--.-", "r": ".-.", 
                "s": "...", "t": "-", "u": "..-", 
                "v": "...-", "w": ".--", "x": "-..-",
                "y": "-.--", "z": "--..", "0" : "-----",
                "1" : ".----" , "2" : "..---" , "3" : "...--",
                "4" : "....-", "5" : ".....", "6" : "-....",
                "7" : "--...", "8" : "---..", "9" : "----.",
                "." : ".-.-.-" , "," : "--..--"
                }
morse_to_str = {".-": "a","-...": "b", "-.-." : "c",
                "-.." : "d", "." : "e", "..-.": "f",
                "--." : "g", "...." : "h", ".." : "i",
                ".---" : "j", "-.-" : "k", ".-.." : "l", 
                "--" : "m",  "-." : "n",  "---" : "o",
                ".--.": "p", "--.-" : "q",".-." : "r", 
                "..." : "s", "-" : "t", "..-" : "u", 
                "...-" : "v",".--" : "w", "-..-" : "x",
                "-.--" : "y", "--.." : "z", "-----" : "0",
                ".----" : "1" , "..---" : "2" , "...--" : "3",
                "....-" : "4", "....." : "5",  "-...." : "6",
                "--..." : "7", "---.." : "8", "----." : "9",
                ".-.-.-" : "." , "--..--" : ","
                }


def inverse(s : str)-> str: 
    return "".join([s[len(s)-1-x] for x in range(len(s))])

def shift(s : str, offset: int = 2)->str:
    return "".join([chr(97 +(ord(x)-97+offset)%26) if 97<=ord(x.lower())<= 122 or 48 <=ord(x)<= 57 or ord(x)== 44 or ord(x)==46 else "" for x in s])

def hexadecimal(s : str)->str: 
    return "".join([format(ord(x),"x") if 97<=ord(x.lower())<= 122 or 48 <=ord(x)<= 57 or ord(x)== 44 or ord(x)==46 else "" for x in s])

def inv_hexadecimal(s : str)->str|Exception:
    # return "".join([ bytes.fromhex(x).decode('utf-8') if 97<=ord(x.lower())<= 122 or 48 <=ord(x)<= 57 or ord(x)== 44 or ord(x)==46 else "?" for x in s])

    try:
        byte_str = bytes.fromhex(s)
        return byte_str.decode('utf-8')
    except:
        raise Exception
def morse(s:str)->str:
    return "  ".join([str_to_morse[x.lower()] if 97<=ord(x.lower())<= 122 or 48 <=ord(x)<= 57 or ord(x)== 44 or ord(x)==46 else "" for x in s])

def inv_morse(s : str)-> str:
   return ("".join([ morse_to_str[x] for x in s.split()]))


