# Q7_GroupTheory_HammingCode.py
"""
Q7: Group Theory & Hamming Code Generator
-----------------------------------------
Generates (7,4) Hamming code from 4-bit data,
introduces a 1-bit error, detects and corrects it.
Also verifies group properties using XOR.
"""

import os
import random

output_path = r"C:\Users\Aryan\DM_IA2_ARYAN_LOMTE\outputs\Q7_output.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
open(output_path, "w").close()

def log_output(text):
    print(text)
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

log_output("=== Q7: Group Theory & Hamming Code Generator ===\n")

# ---------- Group Theory: XOR Verification ----------
log_output("Checking Group Properties under XOR Operation:\n")

elements = [0, 1]
closure = all((a ^ b) in elements for a in elements for b in elements)
identity = any(all((a ^ e) == a for a in elements) for e in elements)
inverses = all(any((a ^ b) == 0 for b in elements) for a in elements)
associative = all(((a ^ b) ^ c) == (a ^ (b ^ c)) for a in elements for b in elements for c in elements)

log_output(f"Closure: {closure}")
log_output(f"Identity: {identity}")
log_output(f"Inverses Exist: {inverses}")
log_output(f"Associative: {associative}")

if all([closure, identity, inverses, associative]):
    log_output("✅ (Z₂, XOR) forms a Group.\n")
else:
    log_output("❌ Group properties not satisfied.\n")

# ---------- Hamming Code Generation ----------
log_output("=== (7,4) Hamming Code Generation ===")
data = input("Enter 4-bit binary message (e.g., 1011): ").strip()
while len(data) != 4 or any(bit not in '01' for bit in data):
    data = input("Invalid input! Enter 4-bit binary message: ").strip()

d1, d2, d3, d4 = map(int, data)
p1 = (d1 ^ d2 ^ d4)
p2 = (d1 ^ d3 ^ d4)
p3 = (d2 ^ d3 ^ d4)
code = [p1, p2, d1, p3, d2, d3, d4]

log_output(f"Original 4-bit data: {data}")
log_output(f"Hamming(7,4) Code: {''.join(map(str, code))}")

# ---------- Introduce and Correct Single-bit Error ----------
error_pos = random.randint(0, 6)
received = code.copy()
received[error_pos] ^= 1
log_output(f"\nError introduced at bit position {error_pos+1}: {''.join(map(str, received))}")

# Compute syndrome bits
s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
s3 = received[3] ^ received[4] ^ received[5] ^ received[6]
syndrome = s1*1 + s2*2 + s3*4

if syndrome == 0:
    log_output("No error detected.")
else:
    log_output(f"Error detected at position: {syndrome}")
    received[syndrome-1] ^= 1
    log_output(f"Corrected Code: {''.join(map(str, received))}")

log_output("\n✅ Output saved to Q7_output.txt")
