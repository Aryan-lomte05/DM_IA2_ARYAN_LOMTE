# Q3_WarshallsAlgorithm.py
"""
Q3: Warshall’s Algorithm for Transitive Closure
------------------------------------------------
Given a relation represented as a 0–1 matrix, implement Warshall’s
algorithm to find its transitive closure.
"""

import os
import numpy as np

output_path = r"C:\Users\Aryan\DM_IA2_ARYAN_LOMTE\outputs\Q3_output.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
open(output_path, "w").close()

def log_output(text):
    print(text)
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

log_output("=== Q3: Warshall’s Algorithm for Transitive Closure ===\n")

# Example relation matrix (user can change)
R = np.array([[1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [0, 0, 0, 1]])

n = len(R)
log_output("Initial Relation Matrix R:")
for row in R:
    log_output(str(row))

# Warshall’s algorithm
for k in range(n):
    log_output(f"\nConsidering intermediate vertex k={k+1}:")
    for i in range(n):
        for j in range(n):
            if R[i][j] == 0 and (R[i][k] and R[k][j]):
                log_output(f"Path found: {i+1} → {k+1} → {j+1}, setting R[{i+1}][{j+1}] = 1")
            R[i][j] = R[i][j] or (R[i][k] and R[k][j])
    log_output("Updated Matrix:")
    for row in R:
        log_output(str(row))

log_output("\nFinal Transitive Closure R*:")
for row in R:
    log_output(str(row))

log_output("\n✅ Output successfully saved to Q3_output.txt")
