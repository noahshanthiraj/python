def upper27(x):
    
    z={'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
        'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N',
        'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
        'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    a=[]
    for k in x:
        if k in z:
            l=z[k]
            a.append(l)
        else:
            a.append(l)
    return "".join(a)

 
def lower27(x):
    z={'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
        'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
        'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
        'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    a=[]
    for k in x:
        if k in z:
            l=z[k]
            a.append(l)
        else:
            a.append(l)
    return "".join(a)

def captial27(x):

    z={'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
        'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N',
        'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
        'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    a = z[x[0]]
    result= a+x[1:]
    return result

def isupper27(x):
        
    for a in x:

        if  97<=ord(a)<=122:

            return False

    return True

def islower27(s):
    
    for x in s:
        if 65<=ord(x)<=90:
            return False
    
    return True

def isalpha27(z):
    for x in z:
        if ord(x)>=97 and ord(x)<=122:
            continue
        elif ord(x)>=65 and ord(x)<=90:
            continue
        else:
            return False
    return True

def isdigit27(z):
    for x in z:
        if ord(x)>=48 and ord(x)<=57:
            continue
        else:
            return False
    return True


def title27(s):
    '
    z="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"

    result = []
    capitalize_next = True

    for char in s:
        if capitalize_next and 'a' <= char <= 'z':
            result.append(chr(ord(char) - 32))
        
            capitalize_next = False
        elif char in z:
            result.append(chr(ord(char) + 32))
            
            
        
        
        else:
            
            result.append(char)

        if char == ' ':
            capitalize_next = True

    return ''.join(result)   

def swapcase27(x):
    result=[]
    for z in x:
        if z in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z":
            result.append(chr(ord(z) - 32))
        elif z in "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z":
            result.append(chr(ord(z) + 32))
        else:
            result.append(z)
    return "".join(result)
            
        
        
        
        


    

    
    
    