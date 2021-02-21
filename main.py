import puzzle

# f = open("./boards/board1.txt", "r")
# f = open("./boards/41invBoard.txt", "r")
# f = open("./boards/62invBoard.txt", "r")
f = open("./boards/solvedBoard.txt", "r")

p = puzzle.Puzzle(f)
# p = puzzle.Puzzle()

print(p.board)
# print(p.player_pos_row, p.player_pos_col)
print("is solved: ", p.is_solved())

# p.move_right()
#  print(p.board)
#  print(p.player_pos_row, p.player_pos_col)
