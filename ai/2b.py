from queue import Queue

def water_jug_bfs(capacity_jug1, capacity_jug2, target):
    visited_states = set()
    q = Queue()

    # Each element in the queue will store: (jug1, jug2, path_taken)
    q.put((0, 0, []))

    while not q.empty():
        jug1, jug2, path = q.get()

        # If this state is already visited, skip it
        if (jug1, jug2) in visited_states:
            continue

        # Mark the state as visited
        visited_states.add((jug1, jug2))

        # Add current state to path
        current_path = path + [(jug1, jug2)]

        # If we found the exact target state
        if (jug1, jug2) == target:
            return current_path

        # All possible next operations
        possible_states = [
            (capacity_jug1, jug2),  # Fill jug1
            (jug1, capacity_jug2),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            # Pour jug1 -> jug2
            (jug1 - min(jug1, capacity_jug2 - jug2), jug2 + min(jug1, capacity_jug2 - jug2)),
            # Pour jug2 -> jug1
            (jug1 + min(jug2, capacity_jug1 - jug1), jug2 - min(jug2, capacity_jug1 - jug1))
        ]

        # Add next states to the queue
        for state in possible_states:
            if state not in visited_states:
                q.put((state[0], state[1], current_path))

    return None  # No solution found

# Example usage
capacity_jug1 = 5
capacity_jug2 = 4
target = (0,2)  # Looking for Jug1 = 0L and Jug2 = 2L

result_path = water_jug_bfs(capacity_jug1, capacity_jug2, target)

if result_path:
    print("Water Jug Solution Path:")
    for step in result_path:
        print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
else:
    print("No solution found.")