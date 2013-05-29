def input_from_file():
    f = open('input.dat', 'r')
    return [int(line.strip()) for line in f.readlines()]
