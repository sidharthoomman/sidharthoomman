
def abbreviate(words):
    b = len(words)   
    x = 1
    new = []
    while x <= b:
        a=''.join(words[x])
        b=''.join(words[x+1])
        if  x == 0:
            new.append(a.upper())
            
        elif (a == ' ' and b.isaplha() is True):
            new.append(b.upper())
        else:
            continue
        x = x + 1
    return(''.join(new))    


abbreviate('S T K')



print(''.join(new))
a='1'
if a.isalpha() is True:
    print ("Hi")
else:
    print ("Bye")
b
temp = abbreviate('Sid is King')
new
temp
words=' Sid is King'
x=0
if words[0].isspace():
    print("Hi")