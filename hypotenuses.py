''' A program that receives a number,
and shows the possible hypotenuses in that range.
And, after, calculates the sum of all possible hypotenuses.

Syntax: Python 3
Author: pedro.bloss
'''
def main():

    def hypotenuses():

        x = int(input('To which number you wish to find the hypotenuses? Insert an integer. '))

        def find_hypotenuses(x):

            hyp=[]
            for c in range(1, x):
                for a in range(1, x):
                    for b in range(1, x):
                        if c*c == (a*a) + (b*b) and c not in hyp:
                            hyp.append(c)
                            print(20*'-', '\n',
                                  ' Since:',
                                  c, '² = ', a, '² + ', b, '²',
                                  '\n',' ','\n',
                                  c, 'is hypotenuse',
                                  '\n', 20*'-',
                                  )
            print(' ', '\n',
                  'The possible hypotenuses, without repetition, from 1 to ', x,
                  'are: ', '\n',
                  hyp,
                  '\n', ' '
                  )
            return hyp
        
        def sum_hyp(hyp):
            s = 0

            for k in range(len(hyp)):
                s += hyp[k]
            return print(' ', '\n',
                         'The sum of all', hyp, ' hypotenuses, without repetition, from 1 to', x,
                         'is ', s,
                         '\n', ' ',
                         '\n', 20*'.',
                         '\n',' '
                         )
        
        hyp = find_hypotenuses(x)

        sum_hyp(hyp)

    hypotenuses()
    
    def question():
        #Asks the user if wants to continue
        
        while True:
            try:
                #Question as input
                Q = str(input('Continue? Y/N '))
                      
                if Q == 'Y' or Q == 'y' or Q == 'yes' or Q == 'Yes' or Q == 'YES':
                    hypotenuses()
                if Q =='N' or Q == 'n' or Q == 'no' or Q == 'No' or Q == 'NO':
                    print('Fim...')
                    break
                    
                while Q != 'Y' or Q != 'y' or Q != 'yes' or Q != 'Yes' or Q != 'YES' or Q != 'N' or Q != 'n' or Q != 'no' or Q != 'No' or Q != 'NO':
                    print('','\n',
                          'Ops! Insert a valid answer. Y/N.',
                          '\n','')
                    
                    Q = str(input('Continue ? Y/N '))
                    if Q == 'Y' or Q == 'y' or Q == 'yes' or Q == 'Yes' or Q == 'YES':
                        hypotenuses()
                    if Q =='N' or Q == 'n' or Q == 'no' or Q == 'No' or Q == 'NO':
                        print('End...')
                        break
                    
            except ValueError:
                print('','\n',
                          'Ops! Insert a valid answer. Y/N.',
                          '\n','')
                if Q == 'Y' or Q == 'y' or Q == 'yes' or Q == 'Yes' or Q == 'YES':
                    hypotenuses()
                if Q =='N' or Q == 'n' or Q == 'no' or Q == 'No' or Q == 'NO':
                    print('End...')
                    break
                    
            else: break
    question()
            

main()
