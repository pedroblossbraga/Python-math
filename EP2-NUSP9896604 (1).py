"""
===================================================================
EP2 - Interpretador para calculo de expressoes aritmeticas - MAC122
BMAC - 2o Semestre de 2019
@author: Pedro Bloss Braga - NUSP 9896604
Professor: Marcilio Sanches

Obs: Inputs como numeros inteiros de 0 a 9
===================================================================
"""
print(__doc__)

'''
OBSERVACOES:


RESUMO:
O programa imita um prompt do python,
em que se podem fazer operacoes de soma, subtracao, multiplicacao e divisao,
com numeros de input de 0 a 9,


COMANDOS IMPORTANTES:
- para finalizar digite no prompt: fim
- para reiniciar o programa chame a funcao: main()
- para printar o progresso e as operacoes dos strings: verbose=True


OBJETIVOS:
Atacar os diferentes de casos de expressoes e atribuicoes:
- variavel = valor
- expressao numerica
- expressao de variaveis
- associar variavel a expressao
- operacoes com variaveis -> usar valores associados

MELHORIAS:
Gostaria de ajustar para quaisquer valores,
mas para isso precisaria fazer outra estrategia de operacoes,
antes da avaliacao da posfixa
'''
from pythonds.basic.stack import Stack

#############################################
#############################################

## defs

def checa_expressao(s):
    x = s.replace('+','').replace('-','').replace('*','').replace('/','').replace(' ','')
    x = x.replace(' ','')
    s = s.replace(' ','')
    tokenList1 = x.split()
    tokenList2 = s.split()
    l=[]
    m=[]
    for token in tokenList1[0]:
        if token not in  "0123456789":
            l.append(token)
    for token in tokenList2[0]:
        if token in '*-+/':
            m.append(token)
    if len(m)>0 and len(l) ==0:
        return True
    else:
        return False
    
##############################################
    
def associa_vars(d, s):
    z = s.replace(' ','')
    ops='*-+/'
    nums='1234567890'
    
    x = z.replace('+','!').replace('-','!').replace('*','!').replace('/','!')
    x = x.split('!')
    # para cada operando, se estiver no dicionario, troca chave pelo valor, dentro do string da expressao
    for item in x:
        if item in d:
            s = s.replace(item, str(d[item])).replace(' ','')
    #print('s: ', s)

    return s
        
                
##############################################
    
def checa_expressao_literal(d, s):
    s = s.replace(' ','')
    ops='*-+/'
    nums='1234567890'
    for char in s:
        if char in ops:
            char = '$'
    x = s.split('$')
    l=[]
    for item in x:
        if item not in d and item not in nums:
            l.append(item)
    if len(l)>0:
        return False
    else: return True
    
##############################################
def checa_numero(s):
    try:
        x = int(s)
        return True
    except:
        return False
#####################################################################
    
def posfix(infixexpr):  
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxwyz" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
#print(posfix('3 * 2'))
#print(posfix("A * B + C * D"))
#print(posfix("( A + B ) * C - ( D - E ) * ( F + G )"))

####################################################################

def avaliaposfix(postfixExpr):
    
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = fazconta(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def fazconta(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    

#############################################################

def checa_invalido(d, s):
    x = s.replace(' ','')
    x =x.replace('+','').replace('*','').replace('-','').replace('/','')

    l=[]
    tokens='1234567890'
    for char in x:
        if char not in tokens:
            l.append(char)
    if len(l)>0 and l[0] not in d:
        print('Erro: ',l[0], ' nao esta definido') 
        return True
    else: return False

#############################

def main(verbose=False):
    '''
    Casos:

    1. Associacao numerica >>>a = 2 >>>a |Out: 2

    2. Expressao aritmetica >>a+b |Out: c = a+b

    3. Associacao expressao >>> a = 2+3 >> a |Out: 5

    4. Associa variavel >> a= 2+b >>b=3 >> a= 5

    '''
    
    d={} # dicionario que guarda variaveis e resultados
    
    while True: #sempre continua com o prompt
        s = str(input(">>>>>>>>"))

        if s == 'fim': #possibilidade de encerrar o prompt
            break

        exp = s.split('=') # divide onde ha o sinal de igual, separando a variavel da expressao referida, se houver

        var = exp[0].replace(' ', '')
        
        # 'a = b+c' -> exp[0] = 'a', exp[1] = 'b+c'
        # variavel: exp[0]
        #expressao: exp[1]

        #checa se eh apenas um numero, e se sim, apenas printa ele
        #checa_numero(var)

        #---------------------------------------------
        """ imprime variaveis ja associadas a valores """
        #if len(s.replace(' ','').split('='))==1 and var in d:
         #   print(d[var])
            
        #checa se ha variaveis nao ainda associadas a valores
        if len(exp)==1:
            checa_invalido(d, exp[0])
        else:
            checa_invalido(d, exp[1])
        #---------------------------------------------
        ######### 1o caso
        """ a= k """
        #ops='+-/*'
        #for char in exp[1]:
         #   if char in ops:
          #      x = exp[1].
        if len(exp) >1 and (len(exp[1].replace(' ','').split('+'))==1 and len(exp[1].replace(' ','').split('-'))==1 and len(exp[1].replace(' ','').split('*'))==1 and len(exp[1].replace(' ','').split('/'))==1):
            if verbose == True:
                print('(1O CASO)')
            
            checa_invalido(d, exp[1])
            
            if checa_numero(exp[1]):
                d.update({exp[0].replace(' ',''):exp[1].replace(' ','')})
                #print('!!!!!!!!!!!')
                if verbose == True:
                    print(d)
            elif '+' not in exp[1] and '-' not in exp[1] and '/' not in exp[1] and '*' not in exp[1]:
                print('Erro: ', exp[1], ' nao esta definido.')
                
        #if len(exp) == 1 and exp[0] in d:
         #   print(d[exp[0]])
        #----------------------------------------------
        ######### 2o caso
        """ int1 + int2 """
        ''' numeros'''
        if len(exp) ==1 and checa_expressao(var):
            checa_invalido(d, var)
            # transforma para input da funcao da posfix()
            inf = []
            for k in range(len(var)):
                inf.append(var[k]+' ')
            inf = str(inf).replace('[','').replace(']','').replace(',','').replace("'","")[:-1]
            
            # converte infixa para posfixa
            pos = posfix(inf)
            if verbose == True:
                print(pos)

            #avalia posfixa
            res = avaliaposfix(pos) # resultado
            if verbose == True:
                    print('resultado: ',res)
            print(res) #expoe resultado
            ''' variaveis '''
        elif len(exp)==1: 
            z = associa_vars(d, exp[0]) #4o caso
            inf = []
            for k in range(len(z)):
                inf.append(z[k]+' ')
            inf = str(inf).replace('[','').replace(']','').replace(',','').replace("'","")[:-1]
            
            # converte infixa para posfixa
            pos = posfix(inf)
            if verbose == True:
                print(pos)

            #avalia posfixa
            res = avaliaposfix(pos) # resultado
            if verbose == True:
                    print('resultado: ',res)
            print(res) #expoe resultado
        #-----------------------------------------------
        ######### 3o caso
        """ a = int1 + int2 """
        
        if len(exp)>1: 
            z = associa_vars(d, exp[1]) #4o caso
            if verbose == True:
                print('EXP[1] 3O CASO::: ', exp[1])
            
        if len(exp)>1 and checa_expressao(z) and not checa_invalido(d, z):
            if verbose == True:
                if verbose == True:
                    print('(3O CASO)')

            x = z.replace(' ','').replace('+','').replace('-','').replace('/','').replace('*','')
    
            for char in x:
                if verbose == True:
                    print('char: ',char)
                if char in d:
                    char = d[char]
                    if verbose == True:
                        print('char:',char, 'd[char]:',d[char])
                    
            # transforma para input da funcao da posfix()
            e = z.replace(' ','')
            inf = []
            for k in range(len(e)):
                inf.append(e[k]+' ')
            inf = str(inf).replace('[','').replace(']','').replace(',','').replace("'","")[:-1]
            
            # converte infixa para posfixa
            pos = posfix(inf)
            if verbose == True:
                print(pos)

            #avalia posfixa
            res = avaliaposfix(pos) # resultado
            if verbose == True:
                print('resultado: ',res)
            
            chave = exp[0].replace(' ','')
            
            d.update({chave:res}) #guarda em d: {var:valor}
            if verbose == True:
                print(d)
        #-------------------------------------------------

#########################################
######################################
main(verbose=False)

if __name__ == 'main':
    print(__doc__)
    main()

        
