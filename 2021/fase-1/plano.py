cota = int(input())
meses = int(input())
gasto = 0

for i in range(meses):
  quantidadeGasta = int(input())
  gasto += quantidadeGasta

cota = (cota* meses+cota) - gasto
print(cota)
