"""
===================================================================
EP3- Classificao de Arquivos com sort - MAC122
BMAC - 2o Semestre de 2019
@author: Pedro Bloss Braga - NUSP 9896604
Professor: Marcilio Sanches
===================================================================
"""

########################################################
############	         IMPORTS        	############
########################################################

import time
from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randrange
from itertools import groupby

########################################################
##########		CLASSES DE ALGPORITMOS		############
########################################################

class PilhaLista:
	''' Pilha como uma lista '''

	#construtor
	def __init__(self):
		self._pilha = []

	def __len__(self):
		return len(self._pilha)

	def is_empty(self):
		return len(self._pilha) == 0

	# empilha novo elemento e
	def push(self, e):
		self._pilha.append(e)

	# retorna elemento do topo da pilha sme retira-lo
	#excecao se a pilha estiver vazia

	def top(self):
		if self.is_empty():
			raise Empty("Pilha vazia. impossivel retornar elemento do topo.")
		return self._pilha[-1]

	#desempilha elemento
	# excecao se pilha vazia
	def pop(self):
		if self.is_empty():
			raise Empty("Pilha Vazia. Impossivel desempilhar ultimo elemento.")
		return self._pilha.pop()

#-------------------------------------------------------
### Quick Nao Recursivo

class QuickNaoRecursivo:

	def __init__(self, lista):
		self.lista= lista
		#self.listaordenada = Quick_Sort(lista)
		#self.tempo = temp
	def __len__(self):
		return len(self.lista)

	def particiona(self, lista, inicio, fim): #lista, inicio, fim):
		i, j = inicio, fim
		lista = self.lista
		pivo = lista[fim]
		while True:
			#auemntado i
			while i < j and lista[i] <= pivo: i = i + 1
			if i < j:
				lista[i], lista[j] = pivo, lista[i]
			else: break
			#diminuindo j
			while i < j and lista[j] >= pivo: j = j - 1
			if i < j: lista[i], lista[j] = lista[j], pivo
			else: break
		print('i: ', i)
		return i

	def Quick_Sort(self): #, lista):
		lista = self.lista
		
		# cria a pilha de sublistas e inicia com lista completa
		Pilha = PilhaLista()
		Pilha.push((0, len(lista) - 1))
		# Repewte ate que a pilha de sub-listas esteja vazia
		while not Pilha.is_empty():
			print("\nPilha = ", Pilha)
			print("Lista = ", lista)
			inicio, fim = Pilha.pop()
			# So particiona se ha mais de 1 elemento

			if fim - inicio >0:
				k = self.particiona(lista, inicio, fim)
				#Empilhe as sub-listas resultantes
				Pilha.push((inicio, k - 1))
				Pilha.push((k + 1, fim))
		#print(lista)
		return lista

#----------------------------------------------------

class QuickRecursivo:
	def __init__(self, lista):
		self.lista= lista
		self.inicio = 0
		self.final = len(self.lista)-1

		#self.listaordenada = Quick_Sort(lista)
		#self.tempo = temp
	def __len__(self):
		return len(self.lista)

	def trocar(self, n, m):
		l = self.lista
		aux = l[n]
		l[n] = l[m]

		l[m] = aux

	def particionar(self, p, r):
		# escolha do pivo
		l = self.lista 
		x = l[p] #primeiro elemento da esquerda
		i = p # destino final do pivo
		j = p + 1 # comecara apos o pivo, contador para percorrer restante do vetor

		while j <= r: # percorre ate fim do vetor
			if l[j] < x:
				i += 1 # encontrei alguem menor que o pivo, procura a frente
				self.trocar(i, j)
			j += 1 # passa para o proximo elemento

		# percorreu o vetor todo, exceto o pivo
		self.trocar(p, i)

		return i # posicao final do pivo

	def QuickSort(self, p, r):
		l = self.lista
		""" escolha de pivo a esquerda """
		# parada
		if p < r:
			q = self.particionar(p, r)
			self.QuickSort(p, q-1) # ordena elementos menores do que pivo

			self.QuickSort(q+1, r) # ordena elementos maiores do que pivo

		return l

#-----------------------------------------------------
# Selection Sort

class Sort:
	def __init__(self, lista):
		self.lista= lista
		#self.listaordenada = Quick_Sort(lista)
		#self.tempo = temp
	def __len__(self):
		return len(self.lista)

	def selection_sort(self):
		lista = self.lista
		for j in range(len(lista)):
			min_index =0 
			for i in range(len(lista)):
				if lista[i] < lista[min_index]:
					min_index = i
			j=0
			if lista[j] > lista[min_index]:
				aux = lista[j]
				lista[j] = lista[min_index]
				lista[min_index] = aux
		return lista


########################################################
###########		      FUNCOES        	################
########################################################

def gera_data_atual():
	""" Funcao qeradora de string da data de execucao
	util para salvar arquivos com nomes diferentes """

	now = datetime.now()
	data = now.strftime("%d%m%Y")
	hora = now.strftime("%H%M%S")
	d1 = str(data+'_'+hora)
	return d1

#-------------------------------------------------
def ordena(d):
	""" Funcao que ordena os tempos de execucao de cada algoritmo """
	print('Ordem Decrescente de tempos')
	print(50*'-')
	l=[]
	for k in d.keys():
		l.append(k)

	for i in range(len(l)):
		print(i+1, ' ', min(l), 'segundos - ', d[min(l)])
		l.remove(min(l))
	print(50*'-')

#----------------------------------------------------

def separa_iniciais(lexnomes, verbose=False):
	""" Funcao que separa em diferentes listas as iniciais dos nomes"""
	i1, i2, i3, i4 = [],[],[],[]

	for i in range(len(lexnomes)):
		i1.append(lexnomes[i][0])
		i2.append(lexnomes[i][1])
		i3.append(lexnomes[i][2])
		i4.append(lexnomes[i][3])

	if verbose==True:
		print('i1:', '\n', i1)
		print('i2:', '\n', i2)
		print('i3:', '\n', i3)
		print('i4:', '\n', i4)

	return i1,i2,i3,i4

#------------------------------------------------------

def EscreveArquivo(lista, nome):
	""" Funcao que gera txt em que cada linha eh um valor de uma dada lista"""

	#nome = 'C:\\Users\\Pedro.braga\\Desktop\\ep3\\output_'+dataatual+'_ep3_nusp9896604.txt'
	#nome = '/home/pedro/Área de Trabalho/ep3/output_'+dataatual+'_ep3_nusp9896604.txt'

	f = open(nome, "a+")

	f.write("LISTA ORDENADA")

	for val in lista:
		f.write( '\n'+ ' ')
		f.write(str(val))
		f.write( '\n'+ ' ')

	f.close()

#------------------------------------------------------

def LeiaArquivo(arquivo):
	l=[]
	try:
		arq = open(arquivo, "r")
	except Exception as e:
		print('Erro em abertura de arquivo: ', e)
		return None

	for linha in arq:
		try:
			l.append(str(linha))
		except Exception as e:
			print('Erro em adicao de linha do arquivo em lista de linhas.')

	return l

#------------------------------------------------------
### Parte do codigo que gera o arquivo a ser classificado

# nomes randomicos
n1 = ["Felicia", "Catulo", "Osmund", "Artmio", "Senizio", "Tilenio"]
n2 = ["Cartuxo", "Olambro", "Romulo", "Ambulo", "Atomon", "Virino"]
n3 = ["Sereno", "Soterno", "Moncoes", "Oscaran", "Topovi", "Talento"]
n4 = ["Lasmia", "Mantega", "Casas", "Lorentao", "Melkioz", "Motivio"]
nn = 6
# gera um registro com NOME[0..39], DATAN[40..47] e IDENT[48..55]
# conteudo randomico baseado em seu NUSP
# pp = '' - gera um registro completo
# pp != '' - gera apenas uma nova datan + ident ou apenas ident
def GeraRegistro(pp):
	global n1, n2, n3, n4, nn
	# nome, datan e IDENT
	nome = n1[randrange(nn)] + ' ' + n2[randrange(nn)] + ' ' + n3[randrange(nn)] + ' ' + n4[randrange(nn)]
	dia = randrange(28) + 1
	mes = randrange(12) + 1
	ano = randrange(17) + 2000
	datan = f'{dia:02}' + '/' + f'{mes:02}' + '/' + f'{ano:04}'
	ident = f'{randrange(100000000000):011}'
	if pp == '':
		# gera um novo registro completo
		registro = nome + ',' + datan + ',' + ident
		return registro
	elif randrange(2) == 0:
		# preserva o nome e gera datan + ident
		campos = pp.split(',')
		registro = campos[0] + ',' + datan + ',' + ident
		return registro
	else:
		# preserva o nome e datan e gera ident
		campos = pp.split(',')
		registro = campos[0] + ',' + campos[1] + ',' + ident
		return registro

#-----------------------------------------
# gera arquivo nomearq com nreg registros

def GeraArquivo(nusp, nomearq, nreg):
	# randomize
	seed(nusp)
	# quantidade de registros - gera 80% do total
	nreg80 = nreg * 80 // 100
	# tabela para guardar registros para repeticao
	tab = ['' for k in range(nreg // 20)] # 5% dos registros
	# abre arquivo para gravacao
	arq = open(nomearq, "w")
	# grava metade dos registros	
	for k in range(nreg80):
		reg = GeraRegistro('')
		arq.write(reg + '\n')
		print(k + 1, " - ", reg)
		# guarda 5% dos registros para repeticao
		if k % 20 == 0:
			# guarda em tab
			tab[k // 20] = reg
	# grava o resto dos 20% dos registros
	cont = nreg80 + 1
	for k in range(len(tab)):
		# para cada registro em tab gera 4 outros
		for j in range(4):
			reg = GeraRegistro(tab[k])
			arq.write(reg + '\n')
			print(cont, " - ", reg)
			cont += 1
	# fecha arquivo
	arq.close()

#------------------------------------------------------------

def encontra_iguais(l):
	""" 
	Funcao que encontra valores consecutivos e iguais na lista, 
	
	e entao retorna lista com as listas que contem valores iguais.
	Essa funcao serah util para quando precisarei identificar onde fazer nova classificacao,
	ja que na ordem em que ha consecutivos iguais, a classificacao nao os diferenciou.
	Seguindo a ordem <nome> -> <ano> -> <mes> -> <dia> -> <id>
	"""
	res = [list(y) for x,y in groupby(l)]

	return res

#-----------------------------------------------------------------

def ordena_classificacao(l, res):
	ind, lam =[],[]
	for k in res:
		if len(k)>1:
			ind, tam = l.index(k[0]), len(k)

			classifica(k)
			

def testa_algoritmos(minha_lista, verbose=True, gera_grafico=True):

	l1, l2, l3 = copia(minha_lista), copia(minha_lista), copia(minha_lista)

	t1 = time.clock() #grava tempo de inicio
	a1 = QuickNaoRecursivo(l1)
	a1.Quick_Sort()
	if not VerifClass(l1):
		print("Classificação Incorreta!")
	t2 = time.clock() #grava tempo de termino

	t3 = time.clock()
	#a2 = Sort(minha_lista)
	#a2.selection_sort()
	lista_aux = l2
	lista_aux.sort()
	if not VerifClass(l2):
		print("Classificação Incorreta!")
	t4 = time.clock()

	t5 = time.clock()
	a3 = QuickRecursivo(l3)
	i, f = a3.inicio, a3.final
	a3.QuickSort(i, f)
	if not VerifClass(l3):
		print("Classificação Incorreta!")
	t6 = time.clock()

	dt1 = t2-t1 #diferenca de tempos
	dt2 = t4-t3
	dt3 = t6-t5

	print(' ', '\n', 'Arquivo após classificação: ', l1, '\n', ' ')

	# guarda tempos em dicionario para posteriormente ordena-los
	tempos = {dt1: 'Quick Nao Recursivo', 
	dt2: 'Selection Sort',
	dt3: 'Quick Recursivo'}


	if verbose==True:
		print(__doc__) # informacoes do programa
		
		print(60*'=', '\n', ' ', '\n', 
				'Tempo do QuickSort NAO Recursivo', dt1, 's.',
				'\n',' ', '\n', 
				'Tempo do Selection Sort: ', dt2, 's.',
				'\n',' ', '\n', 
				'Tempo do Quick Sort  Recursivo: ', dt3, 's.',
				'\n', ' ', '\n', 60*'=')

	ordena(tempos)

	if gera_grafico == True:

		plt.title('Tempos dos Algoritmos')
		plt.bar('Quick Recursivo', dt3, label='Quick Recursivo')
		plt.legend(loc='best')
		plt.bar('Quick Nao Recursivo', dt1, label='Quick Nao Recursivo')
		plt.legend(loc='best')
		plt.bar('Método sort()', dt2, label='Selection Sort')
		plt.legend(loc='best')
		plt.show()

#---------------------------------------------------------------------

def classifica(minha_lista, algoritmo='QuickRecursivo', verbose=True, gera_grafico=False):

	if algoritmo=='QuickNaoRecursivo':
		t1 = time.clock() #grava tempo de inicio
		a1 = QuickNaoRecursivo(minha_lista)
		a1.Quick_Sort()
		t2 = time.clock() #grava tempo de termino

	if algoritmo=='sort':
		t1 = time.clock()
		#a2 = Sort(minha_lista)
		#a2.selection_sort()
		lista_aux = minha_lista
		lista_aux.sort()
		t2 = time.clock()

	if algoritmo=='QuickRecursivo':
		t1 = time.clock()
		a3 = QuickRecursivo(minha_lista)
		i, f = a3.inicio, a3.final
		a3.QuickSort(i, f)
		t2 = time.clock()

	dt= t2-t1 #diferenca de tempos
	
	print(60*'=', '\n', ' ', '\n', 
			'Tempo: ', dt, 's.',
			'\n', ' ', '\n', 60*'=')

#------------------------------------------------
def VerifClass(l):
    return l == sorted(l)

#--------------------------------------------------

def acha_indices(l1, l2):
	aux=[]

	for k in range(len(l2)):
		if l2[k] in l1:
			aux.append(l1.index(l2[k]))
			l1[l1.index(l2[k])] = 0

	print(20*'=', '\n', 'indices: ', aux, '\n', 20*'=')

	return aux
#---------------------------------------------------

def copia(l):
	l2 = []
	for item in l:
		l2.append(item)
	return l2
#--------------------------------------------------


#######################################################################
################             MAIN             #########################
#######################################################################

def main(nusp = 9896604):
	#while True:
	for i in range(1):
		#para testes
		#nome = '/home/pedro/Área de Trabalho/ep3/input.txt' #input_19112019_210144_ep3_nusp9896604.txt'
		#nome_destino ='/home/pedro/Área de Trabalho/ep3/output.txt' #_19112019_210144_ep3_nusp9896604.txt'
		
		
		#Entre com seu NUSP - para randomizar
		nusp = int(input('Entre com seu NUSP - para randomizar: '))
		
		#nusp = 9896604
		# Gera arquivo com uma certa quantidade de registros
		try:
			nome = input("Entre com o nome do arquivo de origem: ")
		except Exception as e:
			print('Erro no nome de origem: ', e, '!')
		try:
			nome_destino= input("Entre com o nome do arquivo de destino: ")
		except Exception as e:
			print('Erro no nome de destino: ', e, '!')

		quant_reg = int(input("Entre com a quantidade de registros:"))
		
		#quant_reg = 20
		GeraArquivo(nusp, nome, quant_reg)

		# guarda data de execucao
		dataatual = gera_data_atual()

		try:
			arq = open(nome, "r")
		except Exception as e:
			print("Erro na abertura do arquivo: ", e)
		# leitura das linhas do arquivo
		tab = arq.readlines()
		arq.close()

		print("Quantidade de registros a classificar: " + str(len(tab)))

		for i in range(len(tab)):
		    tab[i] = tab[i].split(",")
		    tab[i][1] = int(str(tab[i][1][0:2])+str(tab[i][1][3:5]+str(tab[i][1][6:10])))

		print(' ', '\n', 
			'Arquivo antes da classificação: ', tab, '\n', ' ')

		# funcao que classifica com todos algoritmos
		testa_algoritmos(tab)
		
		# escreve txt com tabela ja classificada
		EscreveArquivo(tab, nome_destino)

###########################################################################

#main()

##########################
if __name__ == '__main__':
	print(__doc__)
	main()

##########################



