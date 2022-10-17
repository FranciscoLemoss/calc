print('Bem vindo ao CALC!')

def testarnum(num):
	try:
		return float(num)
	except:
		raise Exception('Número inválido! Aplicação reiniciada!')

def calcula(operador, num1, num2):
	if operador == '+':
		return num1 + num2
	elif operador == '-':
		return num1 - num2
	elif operador == '*':
		return num1 * num2
	elif operador == '/':
		try:		
			return num1 / num2
		except ZeroDivisionError:
			raise Exception('Impossível dividir um número por zero!')

while(True):

	num1 = input('Digite um número ou sair: ').replace(',', '.')
	if num1.lower() == 'sair':
		break
	try:
		num1 = testarnum(num1)
	except Exception as erro:
		print(erro)
		continue

	operador = input('Digite o operador aritmético (+,-,*,/) ou sair: ')
	if operador not in ('+', '-', '*', '/'):
		print('Operador inválido! Aplicação reiniciada!')
		continue
	if operador.lower() == 'sair':
		break 

	num2 = input('Digite outro número ou sair: ').replace(',', '.')
	if num2.lower() == 'sair':
		break
	try:
		num2 = testarnum(num2)
	except Exception as erro:
		print(erro)
		continue

	try:
		print(f'O resultado é {calcula(operador, num1, num2):.2f}\n\nVamos fazer um novo cálculo :)')
	except Exception as erro:
		print(f'{erro}\nAplicação reiniciada!\n')

print('Até mais ver!')
