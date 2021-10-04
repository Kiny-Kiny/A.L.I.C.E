from pickle import dump,load
from os import path, system
system('git pull')
#######################################
# Simples I.A feita utilizando Python.#
#######################################
__Author__ : 'Kiny'
try:
	if path.exists('BotDialog') == True:
		
		with open('BotDialog','rb') as c:
			
			Dialog = load(c)
except:
	
	class Dialog:
		def __init__(self, perguntasOuFalas,respostas):
			self.perguntasOuFalas=perguntasOuFalas
			
			self.respostas = respostas

	Dialog=Dialog(['Olá!', 'Tudo bem?'],['Olá! :D', 'Sim! E com você?'])
	
def save(arch):
	try:
	
		with open('BotDialog','wb') as f:
			
			dump(arch, f)
		
	except Exception as error:
		
		print(str(error))

def conversa(op):
	
	if op not in Dialog.perguntasOuFalas:
		
		perg=input('Alice : Não entendi. O que devo responder? : ')
		
		Dialog.perguntasOuFalas.append(op)
		
		Dialog.respostas.append(perg)
		
#		save(Dialog)
			
	else:
		
		print('Alice : %s'%Dialog.respostas[Dialog.perguntasOuFalas.index(op)])

def main():
	
	while True:
		
		op=input('- Fale ou pergunte sobre qualquer coisa(para sair, digite /sair): ')
		
		if op in ['/sair']:
			
			break
		
		else:
			
			conversa(op)
	
	system('cls||clear');print('Alice : Espero ver você em breve! :)')

if __name__ == '__main__':
	main()
