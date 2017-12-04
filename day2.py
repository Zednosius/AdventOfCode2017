from get_data import get_data

def get_min_and_max(numbers):
    smallest = None
    largest = None
    for num in numbers:
        if smallest == None or smallest > num:
            smallest = num

        if largest == None or largest < num:
            largest = num
    return (smallest, largest)

def get_evenly_divisible_pair(numbers):
    numerator = None
    denominator = None
    datalen = len(numbers)
    for i in range(0, datalen):
        for j in range(i+1, datalen):
            inum, jnum = numbers[i], numbers[j % datalen]

            if inum % jnum == 0:
                numerator = inum
                denominator = jnum

            elif jnum % inum == 0:
                numerator = jnum
                denominator = inum

    return numerator, denominator

def largest_difference(numbers):
    (smallest, largest) = get_min_and_max(numbers)
    return largest-smallest

def even_division(numbers):
    (numerator, denominator) = get_evenly_divisible_pair(numbers)
    return int(numerator/denominator)

def compute_checksum(data, checksum_func):
    checksum = 0
    for row in data:
        checksum += checksum_func(row)
    return checksum





if __name__ == '__main__':
    data = get_data(2, int)

    print("Task 2.1", compute_checksum(data, largest_difference))
    print("Task 2.2", compute_checksum(data, even_division))