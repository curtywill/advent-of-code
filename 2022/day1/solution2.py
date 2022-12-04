from input import day1

arr = day1.split('\n')
maxes = [0, 0, 0] # cannot have negative calories
total = 0
for num in arr:
  if num == '':
    idx = arr.index(min(arr))
    maxes[idx] = maxes[idx] if maxes[idx] > total else total
    total = 0
    continue
  total += int(num)

print(sum(maxes))
