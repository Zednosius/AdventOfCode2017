
def process_line(line, cast=str):
    return map(cast,map(str.strip, line.split()))

def process_data(unprocessed_data, cast=str):
    data = []
    for line in unprocessed_data.splitlines():
        data.append(list(process_line(line, cast)))
    return data


def get_data_from_file(filename, cast=str):
    """Returns data from filename in matrix format if there is more than one line.
    each element will be casted with the cast provided.
    """
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(list(process_line(line, cast))) 
    return data

def get_data(day_num):
    return get_data_from_file("day{}.txt".format(day_num))

def get_data_as_list(day_num, cast):
    return [e for row in get_data_from_file("day{}.txt".format(day_num), cast) for e in row]
