peso = float(input('qual e seu peso?:'))
altura = float (input('qual e sua altura?:'))

#vamos calcular o imc
imc = peso / (altura * altura)
print('seu IMC é: {0}'.format(imc))

#vamos mostrar a classificacao 
if imc <16:
    print('Magreza grave')
elif (imc >=16) and (imc < 17):
    print('Magreza moderada')
elif (imc >=17) and (imc < 18.5):
    print('Magreza leve')
elif (imc >=18.5) and (imc < 25):
    print('Saudavel')
elif (imc >= 25) and (imc <30):
    print('Sobrepeso')
elif(imc >= 30) and (imc < 35):
    print('Obesidade Grau I')
elif(imc >= 35) and (imc < 40):
    print('Obsesidade Grau II')