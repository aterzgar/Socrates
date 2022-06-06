# create a function for Euclidean distance
def euclidean_distance(pt1, pt2):
    distance = 0
    for i in range(0, len(pt1)):
        distance += (pt1[i] - pt2[i])**2
    return distance**0.5
# create a function for manhattan distance
def manhattan_distance(pt1, pt2):
    distance=0
    for i in range(0, len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    return distance
# create a function for hamming distance
def hamming_distance(pt1, pt2):
    distance = 0
    for i in range(0, len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1
    return distance 


print(euclidean_distance([1, 3, 5], [2, 4, 6]))
print(manhattan_distance([1, 3, 5], [2, 4, 6]))
print(hamming_distance([1, 3, 5], [2, 4, 6]))