irma1 = int(input())
irma2 = int(input())
irma3 = int(input())

if irma1 < irma2 and irma3 < irma2: 
  print(irma3)

elif irma1 < irma2 and irma3 > irma2:
  print(irma2)

elif irma1 == irma2 and irma2 == irma3:
  print(irma1)