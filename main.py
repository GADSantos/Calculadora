#Programa descobrir seu um número é par ou ímpar
#Ler um número e mostar o resultado

NumeroRecebido = input("Digite o número que deseja descobrir se é ímpar ou par \n")

NumeroRecebido = int(NumeroRecebido)
                
resultadoNumero = NumeroRecebido % 2

if (resultadoNumero == 0):
  print("Número é par")
elif (resultadoNumero != 0):
  print("Número é ímpar")