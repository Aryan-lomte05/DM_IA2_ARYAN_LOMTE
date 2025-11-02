# Q4_LatticeVerification.py
"""
Q4: Lattice Verification
------------------------
Check if a given partially ordered set forms a lattice.
"""

import os
import numpy as np

output_path = r"C:\Users\Aryan\DM_IA2_ARYAN_LOMTE\outputs\Q4_output.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
open(output_path, "w").close()

def log_output(text):
    print(text)
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

log_output("=== Q4: Lattice Verification ===\n")

# Example poset represented as adjacency matrix (≤ relation)
M = np.array([
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

n = len(M)
elements = [f"a{i+1}" for i in range(n)]

log_output("Poset Relation Matrix:")
for row in M:
    log_output(str(row))

def leq(x, y):  # whether x ≤ y
    return M[x][y] == 1

def find_lub_meet():
    all_good = True
    for i in range(n):
        for j in range(n):
            # Find upper bounds of {i, j}
            upper_bounds = [k for k in range(n) if leq(i, k) and leq(j, k)]
            lower_bounds = [k for k in range(n) if leq(k, i) and leq(k, j)]
            # Find minimal upper bounds (LUB)
            lubs = [u for u in upper_bounds if all(not (leq(v, u) and v != u) for v in upper_bounds)]
            glbs = [l for l in lower_bounds if all(not (leq(l, v) and v != l) for v in lower_bounds)]
            log_output(f"\nPair ({elements[i]}, {elements[j]}):")
            log_output(f"  Upper bounds: {[elements[u] for u in upper_bounds]}")
            log_output(f"  Lower bounds: {[elements[l] for l in lower_bounds]}")
            if len(lubs) == 1 and len(glbs) == 1:
                log_output(f"  LUB = {elements[lubs[0]]}, GLB = {elements[glbs[0]]}")
            else:
                log_output("  ❌ Lattice condition failed for this pair.")
                all_good = False
    return all_good

result = find_lub_meet()
log_output("\n✅ This is a Lattice!" if result else "\n❌ Not a Lattice.")
log_output("\n✅ Output saved to Q4_output.txt")
