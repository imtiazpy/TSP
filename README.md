# Delivery Route Optimization

A bike rider is tasked with delivering gifts to 10 different City Bank branches, starting from the Uttara Branch. However, traffic congestion poses a significant challenge. Every location is connected to every other location, and the rider must visit all of them before returning to the starting point in Uttara. The rider can visit every location only once and has to determine the most optimal route that minimizes fuel consumption.

## Dataset

From the dataset, we have created two graphs. One of which represents the distance between each pair of locations, and the other represents traffic frequencies.

### Branch Information

Here is the information about the City Bank branches:

| Branch ID | Latitude    | Longitude   | Branch Name                      |
|-----------|-------------|-------------|----------------------------------|
| 1         | 23.8728568  | 90.3984184  | Uttara Branch                    |
| 2         | 23.8513998  | 90.3944536  | City Bank Airport                |
| 3         | 23.8330429  | 90.4092871  | City Bank Nikunja                |
| 4         | 23.8679743  | 90.3840879  | City Bank Beside Uttara Diagnostic |
| 5         | 23.8248293  | 90.3551134  | City Bank Mirpur 12               |
| 6         | 23.827149   | 90.4106238  | City Bank Le Meridien             |
| 7         | 23.8629078  | 90.3816318  | City Bank Shaheed Sarani          |
| 8         | 23.8673789  | 90.429412   | City Bank Narayanganj             |
| 9         | 23.8248938  | 90.3549467  | City Bank Pallabi                 |
| 10        | 23.813316   | 90.4147498  | City Bank JFP

### Distance Graph

The distance graph represents the imaginary distance values between branches:

|     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|----|
|  1  | 0 | 4 | 8 | 2 | 6 | 9 | 6 | 5 | 8 |  6 |
|  2  | 4 | 0 | 2 | 5 | 7 | 2 | 6 | 4 | 8 |  5 |
|  3  | 8 | 3 | 0 | 6 | 8 | 9 | 7 | 4 | 6 |  9 |
|  4  | 2 | 5 | 6 | 0 | 4 | 3 | 8 | 6 | 7 |  2 |
|  5  | 6 | 4 | 7 | 6 | 0 | 8 | 6 | 3 | 4 |  2 |
|  6  | 9 | 2 | 3 | 5 | 7 | 0 | 8 | 2 | 4 |  3 |
|  7  | 6 | 4 | 2 | 7 | 8 | 9 | 0 | 4 | 2 |  9 |
|  8  | 5 | 4 | 3 | 2 | 5 | 7 | 8 | 0 | 2 |  7 |
|  9  | 8 | 2 | 5 | 3 | 4 | 7 | 9 | 8 | 0 |  8 |
|  10 | 6 | 4 | 7 | 8 | 9 | 2 | 4 | 3 | 7 |  0 |

### Traffic Frequencies

The traffic frequencies graph represents the additional time per hour it would take to reach a specific location:

|     | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|  1  | 0   | 0.2 | 0.1 | 0.3 | 0.4 | 0.1 | 0.6 | 0.2 | 0.3 | 0.2 |
|  2  | 0.2 | 0   | 0.3 | 0.2 | 0.3 | 0.2 | 0.2 | 0.4 | 0.1 | 0.2 |
|  3  | 0.1 | 0.2 | 0   | 0.4 | 0.1 | 0.2 | 0.2 | 0.3 | 0.1 | 0.2 |
|  4  | 0.3 | 0.2 | 0.3 | 0   | 0.1 | 0.2 | 0.4 | 0.3 | 0.1 | 0.2 |
|  5  | 0.4 | 0.1 | 0.2 | 0.3 | 0   | 0.2 | 0.1 | 0.4 | 0.3 | 0.2 |
|  6  | 0.1 | 0.2 | 0.1 | 0.2 | 0.2 | 0   | 0.1 | 0.3 | 0.4 | 0.2 |
|  7  | 0.6 | 0.1 | 0.4 | 0.3 | 0.2 | 0.2 | 0   | 0.1 | 0.2 | 0.3 |
|  8  | 0.2 | 0.4 | 0.1 | 0.3 | 0.2 | 0.2 | 0.1 | 0   | 0.3 | 0.2 |
|  9  | 0.3 | 0.2 | 0.2 | 0.1 | 0.2 | 0.3 | 0.2 | 0.3 | 0   | 0.1 |
|  10 | 0.2 | 0.3 | 0.2 | 0.2 | 0.3 | 0.2 | 0.1 | 0.4 | 0.1 | 0   |


## Optimization Algorithm

To find the most optimal route that minimizes fuel consumption, an algorithm has been implemented by following the following factors:

1. The rider starts initially with a speed of 50 km/h.
2. The traffic frequency refers to the additional time per hour it would take to reach a specific location. For example, if the traffic frequency is 0.5, it means the rider will need an extra 5 minutes per hour to reach that location.
3. If the distance takes more than 30 minutes at the initial speed of 50 km/h, the speed will increase by 10 km/h for only 5 minutes.