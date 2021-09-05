"""
JPMZ
A group of python functions that change from one numbering 
system to another, and shows the needed steps to 
arithmetically do so.
"""

def dec_hex(x):
    whole = []
    while x:
        b = x % 16
        print("{} /16 = {} > {}".format(x, (x//16), b))
        x = x // 16
        if   b == 10: b = "A"
        elif b == 11: b = "B" 
        elif b == 12: b = "C"
        elif b == 13: b = "D"
        elif b == 14: b = "E"
        elif b == 15: b = "F"
        whole.append(b)
    else:
        whole.reverse()
        print(*whole)  

def hex_bin(x):
    
    resultado = (x.replace(" ","")
                 .replace("0","0000 ")
                 .replace("1","0001 ")
                 .replace("2","0010 ")
                 .replace("3","0011 ")
                 .replace("4","0100 ")
                 .replace("5","0101 ")
                 .replace("6","0110 ")
                 .replace("7","0111 ")
                 .replace("8","1000 ")
                 .replace("9","1001 ")
                 .replace("A","1010 ")
                 .replace("B","1011 ")
                 .replace("C","1100 ")
                 .replace("D","1101 ")
                 .replace("E","1110 ")
                 .replace("F","1111 "))
    
    original = " "
    for i in x.replace(" ",""):
        original += i +" "*(len(resultado) // len(x))
    
    print(original +'\n'+ resultado)
    return resultado
    
def bin_dec(x):
    resultado = potencia = 0
    bits = x.replace(" ","")[::-1]
    for y in bits:
        valor = int(y) * (2**potencia)
        if int(y): 
            print("{} * 2^{} = {}".format(y, potencia, valor))
        #else: print("0")
        resultado += valor
        potencia += 1
    print(resultado)
    return resultado

def dec_bin(x):
    whole = []
    while x:
        b = x % 2
        whole.append(b)
        print(str("{} /2 = {} > {}").format(x,(x//2),b).center(20))
        x = x // 2
    else:
        whole.reverse()
        print(*whole) 
    
def bin_hex(x):
    dec_hex(
        bin_dec(x))
    print("[Done]")
    
def hex_dec(x):
    bin_dec(
        hex_bin(x))  
    print("[Done]")  
