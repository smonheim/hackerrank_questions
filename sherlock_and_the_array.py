def checker(check):
  left = 0
  right = 0
  left_index = 0
  right_index = len(check) - 1
  while right_index - left_index > 0:
    if left > right:
      right += check[right_index]
      right_index -= 1
    else:
      left += check[left_index]
      left_index += 1
  if left == right:
    print "YES"
  else:
    print "NO"
    
n = raw_input().strip()
arr = []
for x in range(int(n)):
  raw_input().strip()
  arr.append(map(int, raw_input().strip().split(' ')))

for x in arr:
  checker(x)
