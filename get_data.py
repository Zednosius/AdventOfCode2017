def get_data_from_file(filename, cast=str):
    """Returns data from filename in matrix format if there is more than one line.
    each element will be casted with the cast provided.
    """
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(list(map(cast,map(str.strip, line.split()))))
    return data
