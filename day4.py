import pandas as pd
import re
import numpy as np

data = pd.read_csv("data/day4.csv", header=None, sep='/n', engine='python')[0]
draw_data = np.array(re.split(",", data[0]), dtype=int)
board_data = data[1:]


class Board:
    def __init__(self, board_nums, size=5):
        self.board_nums = board_nums
        self.size = size
        self.hits = 0
        self.won = False

    def check_for_bingo(self):
        """Checks the vertical and horizontal columns for bingo"""
        if -5 in [sum(row) for row in self.board_nums]:
            return True

        cols = [[row[i] for row in self.board_nums] for i in range(self.size)]
        if -5 in [sum(col) for col in cols]:
            return True

        return False

    def calculate_solution(self, last_number):
        """Returns the score as defined by the puzzle"""
        return (np.sum(self.board_nums) + self.hits)*last_number

    def play_move(self, number):
        """Updates the board state to reflect a specific number
        played"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board_nums[i, j] == number:
                    self.hits += 1
                    self.board_nums[i, j] = -1

    def print_board(self):
        """Prints the board"""
        for col in self.board_nums:
            print(col)


# Challenge 1

boards = []
for i in range(len(board_data)//5):
    nums = np.array([
        [int(s) for s in re.split(r"\s *", board_data[j], 4)]
        for j in range(5*i+1, 5*i+6)])
    boards.append(Board(nums))

winners = []
i = 0
first = 0
for i in range(len(draw_data)):
    for b in boards:
        b.play_move(draw_data[i])
        if b.check_for_bingo() is True and b.won is False:
            winners.append(b.calculate_solution(draw_data[i]))
            b.won = True
print(winners[0])

# Challenge 2

print(winners[-1])
