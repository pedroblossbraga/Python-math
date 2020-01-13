""" Binary number converter:
- converts numbers to binary
- the num() function converts back to the binary, by using the list of divisions and remainders

Example:
>>> binario(5)
(div, res): (2, 1)
(div, res): (1, 0)
(div, res): (0, 1)
binario:  101
([1, 0, 1], [0, 1, 2])
>>> div, res = binario(8)
(div, res): (4, 0)
(div, res): (2, 0)
(div, res): (1, 0)
(div, res): (0, 1)
binario:  1000
>>> num(div, res)
numero:  8
8

"""

def binario(n):
    div,res=[],[]
    s=''
    while n>0:
        print('(div, res):',(n//2, n%2))
        div.append(n%2)
        res.append(n//2)
        n = n//2
    div.reverse()
    res.reverse()
    #print(res)
    for el in div:
        s += str(el)
    print('binario: ', s)
    return div,res

def num(div, res):
     s = sum(div) + sum(res)
     print('numero: ',s)
     return s
    
