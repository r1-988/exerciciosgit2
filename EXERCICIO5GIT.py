#EXERCICIO 05 MODULO GIT/GITHUB.
#PRECISA PASSAR PARA O GIT E DEPOIS PARA O GIT HUB.

sexo = input('OLÁ! VOCÊ É DO SEXO MASCULINO OU FEMININO?').upper()
altura = float(input('LEGAL! INFORME A SUA ALTURA:'))
homem = (72.7*altura)-58
mulher = (62.1*altura)-44.7
if sexo == 'MASCULINO':
    print ('SE VOCE É DO SEXO MASCULINO, LEVANDO EM CONTA A SUA ALTURA, SEU PESO IDEAL É:{:.2f}'.format(homem))
else:
    print ('SE VOCE É DO SEXO FEMININO, LEVANDO EM CONTA A SUA ALTURA, SEU PESO IDEAL É:{:.2f}'.format(mulher))
