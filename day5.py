from get_data import get_data_as_list



def steps_until_escape(jump_maze):
    jump_maze.append("EXIT")
    index = 0
    jumps = 0
    while jump_maze[index] != "EXIT":
        jump_length = jump_maze[index]
        jump_maze[index] += 1
        index += jump_length
        jumps += 1

    return jumps

def steps_until_escape2(jump_maze):
    jump_maze.append("EXIT")
    index = 0
    jumps = 0
    while jump_maze[index] != "EXIT":
        jump_length = jump_maze[index]
        if jump_length >= 3:
            jump_maze[index] -= 1
        else:
            jump_maze[index] += 1
        # print("Jumping with ", jump_length)
        index += jump_length
        jumps += 1

    return jumps

if __name__ == '__main__':
    data = get_data_as_list(5, int)
    print("Task1 jumps: ", steps_until_escape(list(data)))
    # print(steps_until_escape2([0, 3, 0, 1, -3]))
    print("Task2 jumps: ", steps_until_escape2(list(data)))