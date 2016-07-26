n = int(raw_input().strip())
lastans = 0
slist = []
qre =[]
[slist.append(raw_input().strip()) for x in range(n)]
m = int(raw_input().strip())
[qre.append(raw_input().strip()) for x in range(m)]
i = 0
for x in qre:
  for y in slist:
    if x == y:
      i += 1
  print i
  i = 0
