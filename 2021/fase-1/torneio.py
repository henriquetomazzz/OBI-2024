count = 0
for i in range(1, 7, 1):
  jogo = input()
  for x in jogo:
    if x == "V":
      count += 1
if count == 5 or count == 6:
  print("1")
elif count == 3 or count == 4: 
  print("2")
elif count == 1 or count == 2: 
  print("3")
else: 
  print("-1")
  