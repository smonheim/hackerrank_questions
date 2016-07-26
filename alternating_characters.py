n = int(raw_input().strip())
arr = []

for x in range(n):
  arr.append(list(raw_input().strip()))
  
i = 0

while i < len(arr):
  j = 0
  k = 0
  while j < (len(arr[i]) - 1):
    if arr[i][j] == arr[i][j+1]:
      k += 1
    j += 1
  i += 1
  print k
