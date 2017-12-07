import itertools as it



def tuple_sum(xy1, xy2):
    return (xy1[0] + xy2[0], xy1[1] + xy2[1])

def get_index(spiral, xy):
    return spiral.get(xy, 0)

def get_neighbours(xy):
    directions = [(1,0), (0,1),(-1,0),(0,-1) # right,up,left,down
    #diagonals
    ,(1,1),(-1,1),(-1,-1),(1,-1)]

    return map(tuple_sum, directions,  it.repeat(xy))

def calc_cell(spiral, cell):
    s = sum(map(lambda x: get_index(spiral, x), get_neighbours(cell)))
    return s

def move(spiral, cell,  direction):
    cell = tuple_sum(cell, direction)
    spiral[cell] = calc_cell(spiral, cell)
    return spiral, cell

def create_spiral_until_cell_exceeds(num):
    cell = (0,0)
    n = 0
    spiral = {(0,0) : 1}
    while get_index(spiral, cell) < num:
        #Initial step to get into the next spiral level.
        n += 1
        spiral, cell = move(spiral, cell, (1,0))
        if (spiral[cell] > num): return (cell, spiral[cell]) #return if exceed

        steps_up   = int(get_square_nums(n)/4 -1)
        rest = int(get_square_nums(n)/4)

        #Spiral goes, left, down , right square_nums(n)/4 times
        for (length, direction) in [(steps_up, (0,1)) , (rest, (-1,0)), (rest, (0,-1)), (rest, (1,0))]:
            for i in range(0, length):
                spiral, cell = move(spiral, cell, direction)
                if (spiral[cell] > num): return (cell, spiral[cell]) #return if exceed
        

    return (cell, spiral[cell])

def get_square_nums(n):
    "Gets the number of numbers in this square shell. eg. square 1 has 8 numbers, square 2 has 16."
    return n*8

def get_square_max(n):
    "Gets the biggest number in a square shell."
    if n <= 0:
        return 1
    return get_square_nums(n)+get_square_max(n-1)

def get_square_min(n):
    return get_square_max(n-1)+1

def get_right_center(n):
    "Gets the center digit on the right side"
    return get_square_min(n) + (n-1)


def get_top_center(n):
    "Gets the center digit on the top side"
    return get_right_center(n) + int(get_square_nums(n)/4)

def get_left_center(n):
    "Gets the center digit on the left side"
    return get_top_center(n) + int(get_square_nums(n)/4)

def get_bottom_center(n):
    "Gets the center digit on the bottom side"
    return get_square_max(n) - n

def get_centers(n):
    return (get_right_center(n), get_top_center(n), get_left_center(n), get_bottom_center(n))

def get_distance_to_access(datanum, n):
    r,t,l,b = get_centers(n)

    steps_to_center = min(datanum - r, datanum - t, datanum - l, datanum - b)
    #Steps to accesspoint 1 is number of steps to a center then n steps to walk all the way back to 1.
    return steps_to_center + n

def find_square_num(number):
    "Finds the square number resides in. eg. 9 returns 1, 23 returns 2, 26 returns 3"
    n = 0
    maximum = 1
    while maximum < number:
        n += 1
        maximum += get_square_nums(n)
    return n

def print_info(data_num):
    print("For data number: ",data_num)
    n = find_square_num(data_num)
    print("Numbers in square", get_square_nums(n))
    print("Maximum in square", get_square_max(n))
    print("Minimum in square", get_square_min(n))
    print("Right Center", get_right_center(n))
    print("Top Center", get_top_center(n))
    print("Left Center", get_left_center(n))
    print("Bottom Center", get_bottom_center(n))
    print("Distance to Access",get_distance_to_access(data_num, n))


if __name__ == '__main__':
    data = 23
    print_info(6)
    print_info(31)
    print()
    print_info(265149)
    print()

    data = 0

    cell,value = create_spiral_until_cell_exceeds(265149)
    print("Exceeded 265149 at ",cell," With value ", value)

