#EXERCICIO 06 MODULO GIT/GITHUB
#CALCULO DO IMC:
saudacao = float(input('Olá! Vamos calcular o seu IMC! Me informe o seu peso:'))
saudacao1 = float(input('Legal! Agora me informe a sua altura:'))

imc = saudacao / (saudacao1*saudacao1)

print ('Pelos meus calculos, o seu IMC é:{:.2f}'.format(imc))

if imc < 18.50:
    print('Você está abaixo do peso!')
elif imc < 25.00:
    print ('Você está no peso normal!')
elif imc < 30:
    print ('Você está acima do peso!')
else:
    print ('Você está obeso!')

    