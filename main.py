import puzzle

f = open("./boards/board1.txt", "r")

p = puzzle.Puzzle(f)
# p = puzzle.Puzzle()

print(p.board)
print(p.player_pos_row, p.player_pos_col)
# print(p.is_solved())

p.move_right()
print(p.board)
print(p.player_pos_row, p.player_pos_col)