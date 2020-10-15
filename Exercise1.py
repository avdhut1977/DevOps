def calc(op,a,b):
    if op == '+':
        return a+b
    elif op == 'x':
        return a*b
    elif op == '-':
        return a - b
    elif op == '/':
        return a/b

with open('contents.txt', 'r') as f:
    content = f.read().splitlines()
    print (content)

for a in content:

    contents = a.split(' ')
    if contents[0] == 'calc':
        val = calc(contents[1],float(contents[2]),float(contents[3]))
        print(str(val))
    if contents[0] == 'goto' :
        if contents[1] == 'calc':
            val = calc(contents[2],float(contents[3]),float(contents[4]))
            newContent= content[int(val)-1]
        else:
            newContent= content[int(contents[1])-1]   
        print(newContent)     
        
         

