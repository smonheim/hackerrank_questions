n = raw_input().strip()
i = 0
a = []
while True:
  try:
    raw_input().strip()
    d = raw_input().strip().split(" ")
    i = 0
    while i < len(d):
      d[i] = int(d[i])
      i += 1
    a.extend([d])
  except EOFError:
    break
    
i = 0
j = 0
while i < len(a):
  profit = 0
  b = len(a[i])
  c = max(a[i])
  while j < b:
    if (a[i][j]) == c:
      if j + 1 >= b:
        break
      else:
        c = max(a[i][(j+1):])
    else:
      profit += c - a[i][j]
    j += 1

  print profit
  j = 0
  i += 1
