# Greedy Interval Scheduling Algorithm

def find_scheduled_intervals(intervals):
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    scheduled_intervals = []
    current_end_time = 0

    for start, end in intervals:
        # Check if interval can be scheduled without conflict with other intervals
        if start >= current_end_time:
            # If no conflict, schedule the interval and update current end time
            scheduled_intervals.append((start, end))
            current_end_time = max(current_end_time, end)

    return scheduled_intervals


# Example usage:
intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
scheduled_intervals = find_scheduled_intervals(intervals)
print("Scheduled intervals:", scheduled_intervals)