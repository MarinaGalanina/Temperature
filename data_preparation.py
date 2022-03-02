
def load_txt(filename):

    dataset = list()

    f = open(filename, 'r')
    list_of_lines = (f.read()).splitlines()

    for i in range(len(list_of_lines)):
        # parameters[0] = temperature, parameters[1] = wind_speed, parameters[2] = hot or cold
        parameters = list_of_lines[i].split(' ')
        dataset.append([int(parameters[0]), int(parameters[1]), parameters[2]])

    return dataset
