import random

def calculate_heuristic(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(n, max_restarts=1000):
    for _ in range(max_restarts):
        current_board = [random.randint(0, n-1) for _ in range(n)]
        current_heuristic = calculate_heuristic(current_board)

        while True:
            neighbor = None
            min_heuristic = current_heuristic

            for col in range(n):
                for row in range(n):
                    if current_board[col] != row:
                        new_board = list(current_board)
                        new_board[col] = row
                        new_heuristic = calculate_heuristic(new_board)
                        if new_heuristic < min_heuristic:
                            neighbor = new_board
                            min_heuristic = new_heuristic

            if neighbor is None:
                break  # Local minimum
            current_board = neighbor
            current_heuristic = min_heuristic

            if current_heuristic == 0:
                return current_board

    return None  # Failed after max_restarts

# Example usage
n = 10
solution = hill_climbing(n)
if solution:
    print("N-Queens Solution:", solution)
else:
    print("No solution found.")
