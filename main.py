import puzzle

f = open("./boards/board1.txt", "r")

p = puzzle.Puzzle(f)
# p = puzzle.Puzzle()

print(p.board)
print(p.player_position)