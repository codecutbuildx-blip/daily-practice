# Greedy Interval Scheduling
## Problem Description
Given a set of intervals, find the maximum number of non-overlapping intervals that can be scheduled.

## Algorithm Explanation
The greedy algorithm works by sorting the intervals based on their end points and then selecting the non-overlapping intervals greedily.

## Code

```python
def greedy_interval_scheduling(intervals):
    # Sort the intervals based on their end points
    intervals.sort(key=lambda x: x[1])

    # Initialize a list to store the selected intervals
    selected_intervals = [intervals[0]]

    # Iterate over the remaining intervals
    for i in range(1, len(intervals)):
        # Get the last scheduled interval
        last Scheduled_interval = selected_intervals[-1]

        # Check if the current interval overlaps with the last scheduled interval
        if intervals[i][0] >= lastScheduled_interval[1]:
            # If not, add it to the list of selected intervals
            selected_intervals.append(intervals[i])

    return selected_intervals


# Test the function
intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
print(greedy_interval_scheduling(intervals))  # Output: [[1, 3], [5, 7]]