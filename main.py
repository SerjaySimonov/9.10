list=[ ]
N = int(input("Cik bija cilvēku: "))
for i in range(N):
  mass=int(input("Kādā ir viņu masa: "))
  list.append(mass)
listsum=sum(list)
print(listsum)
listavg=sum(list)/len(list)
print(listavg)
if listsum > 300:
  print("Viņi nedrīkst braukt visi kopā")
else:
  print("Viņi drīkst braukt visi kopā")