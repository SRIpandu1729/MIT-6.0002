###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows_file = open(filename, 'r')
    cows_data = cows_file.read()
    cows_data = cows_data.split('\n')
    cows_dict = {}
    for cow in cows_data:
        cows_dict[cow.split(',')[0]] = int(cow.split(',')[1])
    return cows_dict
    pass


def get_next_possible_trip(cows, limit):
    trip = []
    available_weight = limit
    for cow in cows:
        if cow[1] <= available_weight:
            trip.append(cow[0])
            available_weight -= cow[1]
            if available_weight == 0:
                return trip
    return trip


def remove_tripped_cows(cows_iter, trip):
    while len(trip) != 0:
        for i in range(len(cows_iter)):
            if cows_iter[i][0] == trip[0]:
                trip = trip[1:]
                cows_iter.pop(i)
                break
    return cows_iter


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_iter = sorted(cows.iteritems(), key=lambda x: -x[1])
    print cows_iter
    trips = []
    while len(cows_iter) != 0:
        # get the next possible trip
        trip = get_next_possible_trip(cows_iter, limit)
        # append the trip to trips
        trips.append(trip)
        # remove already added cows
        cows_iter = remove_tripped_cows(cows_iter, trip)
    return trips
    pass


def is_valid_partition(cows, partition, limit):
    for trip in partition:
        remaining_weight = limit
        for cow in trip:
            remaining_weight -= cows[cow]
            if remaining_weight < 0:
                return False
    return True


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    is_first_valid_partition = True
    cow_partitions = get_partitions(cows)
    for partition in cow_partitions:
        if is_valid_partition(cows, partition, limit):
            if is_first_valid_partition:
                is_first_valid_partition = False
                number_of_trips = len(partition)
                current_best_partition = partition
            elif len(partition) < number_of_trips:
                number_of_trips = len(partition)
                current_best_partition = partition
    return current_best_partition
    pass


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    greedy_start_time = time.time()
    solution_using_greedy = greedy_cow_transport(load_cows('ps1_cow_data.txt'))
    greedy_end_time = time.time()
    brute_start_time = time.time()
    solution_using_brute = brute_force_cow_transport(load_cows('ps1_cow_data.txt'))
    brute_end_time = time.time()
    print "Time taken by greedy : " + str(greedy_end_time - greedy_start_time)
    print "Number of trips using greedy : " + str(len(solution_using_greedy))
    print "Time taken by brute : " + str(brute_end_time - brute_start_time)
    print "Number of trips using brute : " + str(len(solution_using_brute))
    pass
