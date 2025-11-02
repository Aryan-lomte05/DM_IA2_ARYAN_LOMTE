"""
Q1: Inclusion–Exclusion Principle (Interactive Version)
-------------------------------------------------------
This program:
1. Takes 3 sets (A, B, C) from user input.
2. Displays all intersections and unions step-by-step.
3. Calculates |A ∪ B ∪ C| using both:
   - Direct union method
   - Inclusion–Exclusion formula
4. Automatically saves the full output to outputs/Q1_output.txt
"""

from sympy import FiniteSet
import os

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Redirect output to file
output_path = os.path.join("outputs", "Q1_output.txt")
with open(output_path, "w", encoding="utf-8") as f:

    def out(x):
        print(x)
        f.write(str(x) + "\n")

    # ----------- USER INPUT -----------
    out("Enter elements of Set A (comma separated): ")
    A = FiniteSet(*map(int, input("A = ").split(',')))

    out("Enter elements of Set B (comma separated): ")
    B = FiniteSet(*map(int, input("B = ").split(',')))

    out("Enter elements of Set C (comma separated): ")
    C = FiniteSet(*map(int, input("C = ").split(',')))

    # ----------- CALCULATIONS -----------
    out("\n--- Stepwise Inclusion–Exclusion Calculation ---")

    A_B = A.intersect(B)
    B_C = B.intersect(C)
    A_C = A.intersect(C)
    A_B_C = A.intersect(B.intersect(C))  # ✅ fixed intersection logic
    Union_ABC = A.union(B).union(C)

    term1 = len(A)
    term2 = len(B)
    term3 = len(C)
    term4 = len(A_B)
    term5 = len(B_C)
    term6 = len(A_C)
    term7 = len(A_B_C)

    # Inclusion–Exclusion formula
    IE_value = term1 + term2 + term3 - term4 - term5 - term6 + term7
    Direct_value = len(Union_ABC)

    # ----------- OUTPUT DISPLAY -----------
    out("\nSet A: " + str(A))
    out("Set B: " + str(B))
    out("Set C: " + str(C))

    out("\n|A| = " + str(term1))
    out("|B| = " + str(term2))
    out("|C| = " + str(term3))

    out("|A ∩ B| = " + str(term4))
    out("|B ∩ C| = " + str(term5))
    out("|A ∩ C| = " + str(term6))
    out("|A ∩ B ∩ C| = " + str(term7))

    out("\nStep-by-Step Formula:")
    out(f"|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |B∩C| - |A∩C| + |A∩B∩C|")
    out(f"|A ∪ B ∪ C| = {term1} + {term2} + {term3} - {term4} - {term5} - {term6} + {term7}")

    out(f"\nBy Inclusion–Exclusion = {IE_value}")
    out(f"By Direct Union       = {Direct_value}")

    out("\nVerification: " + ("MATCH ✅" if IE_value == Direct_value else "MISMATCH ❌"))
    out("\nOutput also saved to: " + output_path)

print(f"\n✅ Output successfully saved to {output_path}")
