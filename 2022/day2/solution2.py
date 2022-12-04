from input import day2

score = 0
moves = {
  'A': {
    'X': 3,
    'Y': 4,
    'Z': 8
  },
  'B': {
    'X': 1,
    'Y': 5,
    'Z': 9
  },
  'C': {
    'X': 2,
    'Y': 6,
    'Z': 7
  }
}

for i in range(1, len(day2), 4):
  p1 = day2[i]
  p2 = day2[i+2]
  score += moves[p1][p2]

print(score)