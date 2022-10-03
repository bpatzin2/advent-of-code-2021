import functools

INITIAL_STATE = [0, 0]
HORIZ_STATE = 0
DEPTH_STATE = 1


def to_command(command_str):
    parts = str.split(command_str, " ")
    return [parts[0], int(parts[1])]


def apply_command(current_state, command):
    direction = command[0]
    units = command[1]
    if direction == "forward":
        prev_horizontal = current_state[HORIZ_STATE]
        current_state[HORIZ_STATE] = prev_horizontal + units
    elif direction == "up":
        prev_depth = current_state[DEPTH_STATE]
        current_state[DEPTH_STATE] = prev_depth - units
    elif direction == "down":
        prev_depth = current_state[DEPTH_STATE]
        current_state[DEPTH_STATE] = prev_depth + units
    return current_state


def run():
    file = open("day2-input.txt", "r")
    commandStrs = file.readlines()
    commands = map(to_command, commandStrs)

    final_state = functools.reduce(apply_command, commands, INITIAL_STATE)

    print(final_state)
    result = final_state[HORIZ_STATE] * final_state[DEPTH_STATE]
    print(result)
    return result


if __name__ == "__main__":
    print(run())
