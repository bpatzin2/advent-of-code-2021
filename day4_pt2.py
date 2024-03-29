from more_itertools import split_at
from functools import reduce


def run():
    file = open("day4-input.txt", "r")
    lines = file.read().splitlines()

    number_draws = list(map(int, lines[0].split(",")))
    rest = lines[2:]
    board_strs = list(split_at(rest, lambda a: a == ""))
    boards = list(map(to_board, board_strs))

    print("numbers")
    print(number_draws)
    print("boards")
    print(boards)

    winner_board, numbers = last_winner_with_draw_numbers(boards, number_draws)

    print(winner_board)
    print(numbers)

    s = score(winner_board, numbers)
    print(s)
    return s

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


def to_row(row_str):
    return list(map(int, row_str.strip().split()))


def to_board(board_str):
    return list(map(to_row, board_str))


def is_winning_set(board_numbers, draw_numbers):
    return board_numbers.issubset(draw_numbers)


def get_columns(board):
    result = []
    for i in range(len(board[0])):
        l = list(map(lambda x: x[i], board))
        result.append(l)
    return result


def is_winner(board, numbers):
    number_set = set(numbers)
    for row in board:
        winner = is_winning_set(set(row), number_set)
        if winner:
            return True
    columns = get_columns(board)
    for column in columns:
        winner = is_winning_set(set(column), number_set)
        if winner:
            return True
    return False


def last_winner_with_draw_numbers(boards, number_draws):
    remaining_boards = boards.copy()
    for i in range(len(number_draws)):
        numbers = number_draws[: i + 1]
        still_remaining_boards = []
        for board in remaining_boards:
            if not is_winner(board, numbers):
                still_remaining_boards.append(board)
        if len(still_remaining_boards) == 0:
            return [remaining_boards[0], numbers]
        else:
            remaining_boards = still_remaining_boards
    raise Exception("no winner found")


def score(board, number_draws):
    board_numbers = reduce(lambda x, y: x + y, board)
    unmarked_numbers = diff(board_numbers, number_draws)
    print("unmarked")
    print(unmarked_numbers)
    unmarked_sum = sum(unmarked_numbers)
    last_draw = number_draws[-1]
    print(unmarked_sum)
    print(last_draw)
    return unmarked_sum * last_draw



if __name__ == "__main__":
    print(run())
