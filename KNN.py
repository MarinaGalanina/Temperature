from math import sqrt


# Calculate distance between the point with euclidean metrics
def euclidean_distance(test_vector, train_vector):
    distance = 0.0
    for i in range(len(train_vector) - 1):
        distance += (test_vector[i] - train_vector[i])**2
    return sqrt(distance)


# Calculate distance between the point with manhattan metrics
def manhattan_distance(test_vector, train_vector):
    distance = 0.0
    for i in range(len(train_vector) - 1):
        distance += abs(test_vector[i] - train_vector[i])
    return distance


# Locate the most similar neighbors
def get_neighbors(test_vector, train_vector, k_neighbors):

    # Create list for calculate distances
    distances = list()


    # iterating through all the training data and calculate distance
    for train in train_vector:

     #   dist = manhattan_distance(test_vector, train)
        dist = manhattan_distance(test_vector, train)

        # ([train set], distance)
        distances.append((train, dist))

    # sot by distance
    distances.sort(key=lambda tup: tup[1])

    # create list for k-nearest neighbors
    neighbors = list()

    # add k-nearest neighbors to list (without distance)
    for i in range(k_neighbors):
        neighbors.append(distances[i][0])

    return neighbors


def predict_classification(test_vector, train_vector, k_neighbors):

    # get k-nearest neighbors
    neighbors = get_neighbors(test_vector, train_vector, k_neighbors)

    # get class from k-nearest neighbors
    output_values = [row[-1] for row in neighbors]

    prediction = max(set(output_values), key=output_values.count)

    return prediction

