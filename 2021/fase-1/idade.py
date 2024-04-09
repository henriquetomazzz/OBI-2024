irma1 = int(input())
irma2 = int(input())
irma3 = int(input())

lista = [irma3, irma2, irma1]

lista.sort(reverse=True)

if irma1 > irma2 and irma1 > irma3: 
  up = irma1

elif irma2 < irma2 and irma3 > irma2:
  up = irma2

else:
  up = 3

print(sorted(lista)[-2])
