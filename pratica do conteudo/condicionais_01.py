# pedindo a idade do usuário e o ingresso: 
idade_usuario = int(input('Qual a sua idade? '));
tem_ingresso = input('Possui ingresso? ');

if idade_usuario.isalpha():
	print('Entrada inválida. Digite apenas dígitos!')
else:
	pass

# trabalhando as condições: idade.
if idade_usuario >= 18 and (tem_ingresso == 'sim' or tem_ingresso == 'Sim'):
	print('Você pode entrar! ')
elif idade_usuario <= 18 :
	print('Você não pode entrar! Não tem idade! ')
elif idade_usuario >= 18 and (tem_ingresso == 'não' or tem_ingresso == 'Não'):
	print('Você não pode entrar! Não tem ingresso!')

