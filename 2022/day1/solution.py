from input import day1

arr = day1.split('\n')
max = 0 # cannot have negative calories
sum = 0
for num in arr:
  if num == '':
    max = sum if sum > max else max
    sum = 0
    continue
  sum += int(num)

print(max)
