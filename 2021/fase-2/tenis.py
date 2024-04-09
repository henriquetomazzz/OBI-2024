tenis = []

for i in range(4):
  tenis.append(int(input()))

tenis.sort()

print(abs((tenis[3]+tenis[0]) - (tenis[2]+tenis[1]))) 
