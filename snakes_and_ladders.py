cases = raw_input().strip()
snek = {}
ladeh = {}
keep = []
storage = []
for tests in xrange(int(cases)):
  ladders = raw_input().strip()
  for lad in xrange(int(ladders)):
    i,j = raw_input().strip().split(' ')
    ladeh.update({int(i):int(j)})
  snakes = raw_input().strip()
  for sk in xrange(int(snakes)):
    i,j = raw_input().strip().split(' ')
    snek.update({int(i):int(j)})
  storage.append(snek)
  storage.append(ladeh)
  keep.append(storage)
  storage = []
  snek = {}
  ladeh = {}

k = 0
while k < len(keep):
  jump = {}
  for x in keep[k]:
    jump.update(x)
  end = 100
  start = {1}
  steps = 0
  while end not in start:
    steps += 1
    old_start = start
    start = set()
    for x in old_start:
      for roll in range(1,7):
        new_start = x + roll
        start.add(jump.get(new_start, new_start))
  k += 1
  print steps
