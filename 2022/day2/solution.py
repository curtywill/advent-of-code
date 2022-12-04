from input import day2

score = 0

def get_game_outcome(p1, p2):
  if p2 == p1:
    return 3
  if p2 == 1:
    return 6 if p1 == 3 else 0
  if p2 == 2:
    return 6 if p1 == 1 else 0
  if p2 == 3:
    return 6 if p1 == 2 else 0

moves = {
  'A': 1, # rock
  'X': 1,
  'B': 2, # paper
  'Y': 2,
  'C': 3, #scissor
  'Z': 3
}

for i in range(1, len(day2), 4):
  p1 = day2[i]
  p2 = day2[i+2]
  score += moves[p2] + get_game_outcome(moves[p1], moves[p2])

print(score)