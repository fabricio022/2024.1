#n1 = float(input('DIGITE UM NÚMERO: '))
#n2 = float(input('DIGITE OUTRO NÚMERO: '))
#soma = (n1+n2)
#subtraçao = (n1-n2)
#multiplicaçao = (n1*n2)
#divisao = (n1/n2)
#print("A soma entre os valores é: {}\n. A subtração entre os valores é: {}\n. A multiplição entre os valores é: {}\n. A divisão entre oe valores é {:.2f}\n.".format(soma,subtraçao,multiplicaçao,divisao))

a = int(input('DIGITE UM NÚMERO: '))
b = int(input('DIGITE UM NÚMERO: '))
r1 = a>b
r2 = a<b
r3 = a!=b
r4 = a==b
print('a>b --> [{}]\n'.format(r1), 'a<b --> [{}]\n'.format(r2), 'a!=b --> [{}]\n'.format(r3), 'a=b --> [{}]\n'.format(r4))