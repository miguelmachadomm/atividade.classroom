nota = int(input('digite a nota do aluno:'))

if nota >= 90:
    print('A - excelencia')
elif nota >= 80:
    print ('B - muito bom')
elif nota >= 70:
    print('C - bom')
elif nota >= 60:
    print('D - regular')
else:
    print('F - reprovado')