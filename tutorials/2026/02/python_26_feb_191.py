# Greedy Interval Scheduling Algorithm

def greedy_interval_scheduling(intervals):
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    # Initialize the result with the first interval
    result = [intervals[0]]

    # Iterate over the intervals
    for current_interval in intervals[1:]:
        # Get the last interval in the result
        last_interval = result[-1]

        # Check if the current interval starts before the last interval ends
        if current_interval[0] >= last_interval[1]:
            # Add the current interval to the result
            result.append(current_interval)

    return result

# Test the algorithm
intervals = [
    (1, 4),
    (2, 5),
    (3, 6),
    (5, 7),
    (6, 8),
    (7, 9),
    (8, 10),
    (12, 14),
    (13, 15),
    (14, 16)
]

result = greedy_interval_scheduling(intervals)
print("Greedy Interval Scheduling Result:")
for interval in result:
    print(interval)