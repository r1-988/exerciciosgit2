#EXERCICIO 07 GIT/GITHUB
#CALCULO PORCENTAGEM DO PRODUTO:

compra = input('Bem vindo a nossa loja. Ficamos felizes com a sua compra, iremos processar o seu pagamento, OK?').upper()
if compra == 'OK':
    print ('Ok! Vamos lá...')
valor = float(input('Me informe o valor do seu sofá:'))

confirma = input(' O valor do seu sofá é R${}, correto?'.format(valor)).upper()
if confirma == 'SIM':
    print ('Obrigado por confirmar!')
desconto = input ('Me informe a modalidade de pagamento:').upper()
if desconto == 'A VISTA':
    print ('O valor do seu sofá é R${}, pagando avista recebe desconto de 15 por cento e fica R$:{}'.format(valor,valor-(valor*15/100)))
if desconto == 'NO CARTAO A VISTA':
    print ('O valor do seu sofá é R${}, pagando a vista no cartao recebe desconto de 10 por cento e fica R$:{}'.format(valor,valor-(valor*10/100)))
if desconto == '2 VEZES NO CARTÃO':
    print ('O valor do seu sofá é de R${}. Em 2x no cartão, o preço permanece R${}'.format(valor,valor))
if desconto == 'MAIS DE 2 VEZES NO CARTAO':
    print ('Pagando em mais de 2x, haverá acrescimo de 10 por cento no valor. Você pagará R${}'.format (valor+(valor*10/100)))    
print ('A gradecemos pela compra e volte sempre!')