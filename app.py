"""
A bike rider is tasked with delivering gifts to 10 different City Bank branches, starting from the Uttara Branch. However, traffic congestion poses a significant challenge. Every location is connected to every other locations, and the rider must visit all of them before returning to the starting point in Uttara. The rider can visit every location only once and has to determine the most optimal route that minimizes fuel consumption.

================================================================

From the dataset we have created two graphs. One of which represents the distance between each pair of location, and the other represents traffic frequencies.

======================================================================================

Some factors added to consider are:
1. Our rider starts initially with a speed of 50 km/h.
2. The traffic frequency refers to the additional time per hour it would take to reach a specific location. For example, if the traffic_frequency is 0.5, it means the rider will need an extra 5 minutes per hour to reach that location.
3. If the distance takes more than 30 minutes at the initial speed of 50 km/h, the speed will increase by 10 km/h for only 5 minutes.

================================================================================

dataset = {
    1: {
        "latitude": 23.8728568,
        "longitude": 90.3984184,
        "branch": "Uttara Branch", 
    },
    2: {
        "latitude": 23.8513998,
        "longitude": 90.3944536,
        "branch": "City Bank Airport", 
    },
    3: {
        "latitude": 23.8330429,
        "longitude": 90.4092871,
        "branch": "City Bank Nikunja", 
    },
    4: {
        "latitude": 23.8679743,
        "longitude": 90.3840879,
        "branch": "City Bank Beside Uttara Diagnostic", 
    },
    5: {
        "latitude": 23.8248293,
        "longitude": 90.3551134,
        "branch": "City Bank Mirpur 12", 
    },
    6: {
        "latitude": 23.827149,
        "longitude": 90.4106238,
        "branch": "City Bank Le Meridien", 
    },
    7: {
        "latitude": 23.8629078,
        "longitude": 90.3816318,
        "branch": "City Bank Shaheed Sarani", 
    },
    8: {
        "latitude": 23.8673789,
        "longitude": 90.429412,
        "branch": "City Bank Narayanganj", 
    },
    9: {
        "latitude": 23.8248938,
        "longitude": 90.3549467,
        "branch": "City Bank Pallabi", 
    },
    10: {
        "latitude": 23.813316,
        "longitude": 90.4147498,
        "branch": "City Bank JFP", 
    }
}
"""

import itertools


# define the number of branches
n = 10

# distances graph with imaginary distance values between branches
distances = [
  [0, 4, 8, 2, 6, 9, 6, 5, 8, 6],
  [4, 0, 2, 5, 7, 2, 6, 4, 8, 5],
  [8, 3, 0, 6, 8, 9, 7, 4, 6, 9],
  [2, 5, 6, 0, 4, 3, 8, 6, 7, 2],
  [6, 4, 7, 6, 0, 8, 6, 3, 4, 2],
  [9, 2, 3, 5, 7, 0, 8, 2, 4, 3],
  [6, 4, 2, 7, 8, 9, 0, 4, 2, 9],
  [5, 4, 3, 2, 5, 7, 8, 0, 2, 7],
  [8, 2, 5, 3, 4, 7, 9, 8, 0, 8],
  [6, 4, 7, 8, 9, 2, 4, 3, 7, 0]
]

"""
Let's understand how to read from the above graph.
On the first row each value represents the distance between Branch-1 to every other branches.
1 to 1 = 0
1 to 2 = 4
.
.
1 to 10 = 6

similarly on the second row 
2 to 1 = 4
20 to 2 = 0
.
.
2 to 10 = 5
"""

# traffic_frequencies graph with imaginary values between branches
traffic_frequencies = [
    [0, 0.2, 0.1, 0.3, 0.4, 0.1, 0.6, 0.2, 0.3, 0.2],
    [0.2, 0, 0.3, 0.2, 0.3, 0.2, 0.2, 0.4, 0.1, 0.2],
    [0.1, 0.2, 0, 0.4, 0.1, 0.2, 0.2, 0.3, 0.1, 0.2],
    [0.3, 0.2, 0.3, 0, 0.1, 0.2, 0.4, 0.3, 0.1, 0.2],
    [0.4, 0.1, 0.2, 0.3, 0, 0.2, 0.1, 0.4, 0.3, 0.2],
    [0.1, 0.2, 0.1, 0.2, 0.2, 0, 0.1, 0.3, 0.4, 0.2],
    [0.6, 0.1, 0.4, 0.3, 0.2, 0.2, 0, 0.1, 0.2, 0.3],
    [0.2, 0.4, 0.1, 0.3, 0.2, 0.2, 0.1, 0, 0.3, 0.2],
    [0.3, 0.2, 0.2, 0.1, 0.2, 0.3, 0.2, 0.3, 0, 0.1],
    [0.2, 0.3, 0.2, 0.2, 0.3, 0.2, 0.1, 0.4, 0.1, 0]
]

"""Similarly traffic_frequencies has the same relations as distances"""


def calculate_total_travel_time(route, speed, distances, traffic_frequencies):
    total_time = 0
    current_speed = speed 

    # Calculate the travel time for each leg of the route
    for i in range(len(route) - 1):
        source = route[i] - 1
        destination = route[i + 1] - 1

        # Calculate the adjusted speed based on the traffic frequency
        adjusted_speed = current_speed * (1 + traffic_frequencies[source][destination])

        # Calculate the travel time for this leg
        travel_time = distances[source][destination] / adjusted_speed

        # Update total time
        total_time += travel_time

        # Check if current speed needs to be increased temporarily
        if travel_time > 0.5:
            current_speed += 10
            # Add the additional time for speed increase
            total_time += 5 / current_speed

    return total_time

# Generate all possible permutations of the branches
branches = list(range(1, n + 1))
permutations = list(itertools.permutations(branches))


# Find the route with minimum travel time
min_travel_time = float('inf')
optimal_route = None
speed = 50

# Iterate through all the permutations and calculate the travel time
for route in permutations:
    # Add the starting and ending point (Uttara)
    route = (0, ) + route + (0, )
    travel_time = calculate_total_travel_time(route, speed, distances, traffic_frequencies)

    # Update the minimum travel time and optimal route if a better solution is found
    if travel_time < min_travel_time:
        min_travel_time = travel_time
        optimal_route = route



print("This is a brute-force solution, which may take a long time for big input.")
print("Optimal Route: ", optimal_route)
print(f"Minimum Travel Time: {min_travel_time} hours")