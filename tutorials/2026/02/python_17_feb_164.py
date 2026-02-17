def find_intervals(tasks):
    # Sort tasks by their end times
    sorted_tasks = sorted(tasks, key=lambda task: task['end'])

    # Initialize variables to store the result and the current time
    schedule = []
    time = 0

    for task in sorted_tasks:
        # If the task starts after the current time, update the time
        if time < task['start']:
            time = task['start']

        # Add the task to the schedule and update the time
        schedule.append((task['id'], task['start'], task['end']))
        time = max(time, task['end'])

    return schedule

# Example usage:
tasks = [
    {'id': 1, 'start': 0, 'end': 2},
    {'id': 2, 'start': 1, 'end': 4},
    {'id': 3, 'start': 3, 'end': 5},
    {'id': 4, 'start': 6, 'end': 7}
]

schedule = find_intervals(tasks)
for task in schedule:
    print(f"Task {task[0]}: ({task[1]}, {task[2]})")