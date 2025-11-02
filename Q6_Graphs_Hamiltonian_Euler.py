# Q6_Hamiltonian_Euler.py
"""
Q6: Hamiltonian Path & Euler Circuit Detector
---------------------------------------------
Determines whether a given graph (via adjacency matrix)
has a Hamiltonian Path or an Euler Circuit.
Also prints all Hamiltonian paths if any exist.
"""

import os
import itertools

output_path = r"C:\Users\Aryan\DM_IA2_ARYAN_LOMTE\outputs\Q6_output.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
open(output_path, "w").close()

def log_output(text):
    print(text)
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

log_output("=== Q6: Hamiltonian Path & Euler Circuit Detector ===\n")

# -------- Adjacency Matrix Input (example graph) --------
G = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
n = len(G)
vertices = list(range(n))

log_output("Adjacency Matrix:")
for row in G:
    log_output(str(row))

# -------- Euler Circuit Check --------
degrees = [sum(G[i]) for i in range(n)]
even_degrees = all(d % 2 == 0 for d in degrees)
connected = True  # assume connected for now

log_output("\nVertex Degrees: " + str(degrees))
if even_degrees and connected:
    log_output("✅ Euler Circuit Exists (all vertices have even degree)")
else:
    log_output("❌ Euler Circuit Does Not Exist")

# -------- Hamiltonian Path Finder (Backtracking) --------
def is_valid(v, pos, path):
    if G[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_util(path, pos):
    if pos == n:
        if G[path[pos-1]][path[0]] == 1:
            return [path + [path[0]]]
        else:
            return [path]
    paths = []
    for v in range(n):
        if is_valid(v, pos, path):
            new_path = path + [v]
            paths.extend(hamiltonian_util(new_path, pos + 1))
    return paths

log_output("\nSearching for Hamiltonian Paths...")
all_paths = []
for start in range(n):
    all_paths.extend(hamiltonian_util([start], 1))

unique_paths = []
for p in all_paths:
    if p not in unique_paths:
        unique_paths.append(p)

if unique_paths:
    log_output(f"\n✅ Hamiltonian Paths Found ({len(unique_paths)}):")
    for path in unique_paths:
        log_output(" → ".join(str(v+1) for v in path))
else:
    log_output("\n❌ No Hamiltonian Paths found.")

log_output("\n✅ Output saved to Q6_output.txt")
