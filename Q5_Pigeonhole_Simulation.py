"""
Q5: Pigeonhole Principle (Deterministic Demo)
---------------------------------------------
If 200 pigeons are placed into 199 holes,
at least one hole will have more than one pigeon.
This version distributes sequentially for clarity.
"""

import os

os.makedirs("outputs", exist_ok=True)
output_path = os.path.join("outputs", "Q5_output.txt")

with open(output_path, "w", encoding="utf-8") as f:
    def out(x):
        print(x)
        f.write(str(x) + "\n")

    pigeons = 24
    holes = 20

    out(f"=== Q5: Deterministic Pigeonhole Principle ===\n")
    out(f"Total Pigeons = {pigeons}, Total Holes = {holes}\n")

    # Sequential deterministic distribution
    assignments = {i: [] for i in range(1, holes + 1)}
    for pigeon in range(1, pigeons + 1):
        hole_num = ((pigeon - 1) % holes) + 1
        assignments[hole_num].append(pigeon)

    # Display holes with pigeon numbers
    overfilled = []
    for h, pigeons_in_hole in assignments.items():
        count = len(pigeons_in_hole)
        out(f"Hole {h}: {pigeons_in_hole} (Count={count})")
        if count > 1:
            overfilled.append(h)

    out(f"\nHoles exceeding capacity: {len(overfilled)}")
    out(f"Overfilled Holes: {overfilled}")

    if len(overfilled) > 0:
        out("\n✅ Pigeonhole Principle holds: at least one hole has ≥ 2 pigeons.")
    else:
        out("\n❌ Unexpected: no overfilled hole found (should not happen).")

out(f"\n✅ Output saved to {output_path}")
