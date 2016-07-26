n = int(raw_input().strip())
arr_a = map(int, raw_input().strip().split(' '))

m = int(raw_input().strip())
arr_b = map(int, raw_input().strip().split(' '))

di_b = dict((el,0) for el in arr_b)
di_a = dict((el,0) for el in arr_b)

ans_arr = []

for x in range(n):
  if arr_a[x] in di_b:
    di_a[arr_a[x]] += 1

for x in range(m):
  if arr_b[x] in di_b:
    di_b[arr_b[x]] += 1
    

for key in di_a:
  if di_a[key] < di_b[key]:
    if not (key in ans_arr):
      print key,
