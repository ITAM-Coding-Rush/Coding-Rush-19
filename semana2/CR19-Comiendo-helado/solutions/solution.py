arr = [0]*11
amigos = int(input())

for i in range(amigos):
  cant = int(input())
  arr[cant]= arr[cant]+1;

for i in range(len(arr)):
  print(str(i)+ " scoops: "+ str(arr[i]))