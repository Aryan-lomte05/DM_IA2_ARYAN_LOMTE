# -*- coding: utf-8 -*-
"""
main.py — Master Runner for DM IA2
----------------------------------
Runs all module programs (Q1–Q7) sequentially and verifies outputs.
"""

import os
import importlib.util
from time import sleep

# Use raw strings (r"...") to avoid Unicode escape issues
BASE_DIR = r"C:\Users\Aryan\DM_IA2_ARYAN_LOMTE"
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# List of all module files
MODULES = [
    "Q1_SetTheory_InclusionExclusion",
    "Q2_Logic_Quantifier_Induction",
    "Q3_Relations_TransitiveClosure",
    "Q4_Lattice_Verification",
    "Q5_Pigeonhole_Simulation",
    "Q6_Graphs_Hamiltonian_Euler",
    "Q7_GroupTheory_HammingCode"
]

def run_module(module_name):
    """Safely import and execute each question script."""
    print(f"\n▶ Running {module_name}.py ...")
    try:
        file_path = os.path.join(BASE_DIR, f"{module_name}.py")
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(f"✅ {module_name} executed successfully.")
    except Exception as e:
        print(f"❌ Error in {module_name}: {e}")
    sleep(1)

def verify_outputs():
    """Check for existence of all output files."""
    print("\n📂 Verifying output files...")
    for i in range(1, 8):
        fname = f"Q{i}_output.txt"
        fpath = os.path.join(OUTPUT_DIR, fname)
        if os.path.exists(fpath):
            print(f"✅ Found {fname}")
        else:
            print(f"⚠️ Missing {fname}")

def main():
    print("🚀 Starting Discrete Mathematics IA2 – Auto Runner\n")
    for mod in MODULES:
        run_module(mod)

    verify_outputs()
    print("\n🎯 All modules executed. Check the 'outputs' folder for results.\n")

if __name__ == "__main__":
    main()
