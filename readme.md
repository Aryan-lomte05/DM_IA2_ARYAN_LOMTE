# 🧮 Discrete Mathematics Automation Project – IA2  
### “Mathematics is not about numbers, equations, or algorithms: it’s about understanding.” — William Paul Thurston  

---

## 👨‍🎓 Author  
**Name:** Aryan Lomte  
**Branch:** Computer Science & Business Systems (CSBS)  
**Subject:** Discrete Mathematics – Internal Assessment 2  
**Institute:** K. J. Somaiya School of Engineering  

---

## 🧠 Project Overview  

This repository presents a comprehensive **Discrete Mathematics Automation Suite** developed in **Python**, designed to computationally demonstrate the core principles of discrete mathematical reasoning.  
It encapsulates seven independent yet interlinked modules, each addressing a fundamental area of discrete mathematics — from foundational set operations to advanced algebraic and graph-theoretical structures.  

Each module automates a distinct concept, simulating the theoretical logic, algorithmic process, and final evaluation through verified computation.  
All programs generate structured outputs in `.txt` files, ensuring reproducibility and clarity of results.  

---

## 🧩 Table of Contents  

| Module | Conceptual Domain | Topic | Challenge Level |
|:-------:|:------------------|:------|:----------------:|
| **Q1** | Set Theory | Inclusion–Exclusion Principle | 🔸 Moderate |
| **Q2** | Logic & Proofs | Quantifiers & Mathematical Induction Verifier | 🔹 High |
| **Q3** | Relations | Warshall’s Algorithm for Transitive Closure | 🔹 High |
| **Q4** | Posets & Lattices | Lattice Verification | 🔺 Very High |
| **Q5** | Functions & Principles | Extended Pigeonhole Simulation | 🔸 Medium–High |
| **Q6** | Graph Theory | Hamiltonian Path & Euler Circuit Detector | 🔺 Very High |
| **Q7** | Algebraic Structures | Group Theory & (7,4) Hamming Code Generator | 🔺 Extreme |

---

## ⚙️ Technical Architecture  

Each problem has been modularized into its own script, maintaining **single-responsibility design** and **consistent I/O format**.  

DM_IA2_ARYAN_LOMTE/
│
├── main.py → Runs all modules sequentially
├── Q1_SetTheory_InclusionExclusion.py
├── Q2_Logic_Quantifier_Induction.py
├── Q3_Relations_TransitiveClosure.py
├── Q4_Lattice_Verification.py
├── Q5_Pigeonhole_Simulation.py
├── Q6_Graphs_Hamiltonian_Euler.py
├── Q7_GroupTheory_HammingCode.py
│
└── outputs/
├── Q1_output.txt
├── Q2_output.txt
├── Q3_output.txt
├── Q4_output.txt
├── Q5_output.txt
├── Q6_output.txt
└── Q7_output.txt

yaml
Copy code

Each module automatically:
- Executes computation.
- Prints stepwise derivations.
- Logs outputs to its respective `.txt` file inside `/outputs`.

---

## 🧪 Mathematical Coverage  

| Concept | Computational Focus | Outcome |
|----------|--------------------|----------|
| **Set Theory** | Inclusion–Exclusion over 3 finite sets | Union cardinality verification |
| **Predicate Logic** | ∀ / ∃ quantifier simulation, induction validation | Proof-by-verification |
| **Relations** | Warshall’s transitive closure on digraphs | Reflexive closure visualization |
| **Lattice Theory** | LUB/GLB existence for all element pairs | Lattice validation report |
| **Pigeonhole Principle** | Random pigeon assignment with collision analysis | Probabilistic demonstration |
| **Graph Theory** | Recursive Hamiltonian path enumeration & Eulerian check | Graph traversal reasoning |
| **Group Theory** | XOR-based group property test & Hamming (7,4) code | Binary algebra & error correction |

---

## 🚀 Execution  

To run all modules and generate outputs automatically:

```bash
python main.py
Each script can also be executed individually for focused testing:

bash
Copy code
python Q3_Relations_TransitiveClosure.py
🧭 Output Format Example
Each output file provides:

Concept Header

Inputs (either user-defined or random)

Stepwise Computation Process

Final Result and Verification

Status: MATCH ✅ / FAIL ❌

Example excerpt (Q1_SetTheory_InclusionExclusion.py):

mathematica
Copy code
|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |B∩C| - |A∩C| + |A∩B∩C|
|A ∪ B ∪ C| = 3 + 4 + 5 - 2 - 1 - 1 + 1
By Inclusion–Exclusion = 9
By Direct Union       = 9
Verification: MATCH ✅
🧩 Libraries Used
SymPy – symbolic mathematics, sets, and logic simplification

NumPy – matrix manipulation for relations and graphs

NetworkX – graph representation (for Hamiltonian/Euler checks)

Random – pigeonhole simulation

itertools – combinatorial enumeration for graph paths

🧬 Theoretical Significance
This project bridges the axiomatic rigor of discrete mathematics with the applied logic of computer science.
It validates classical mathematical reasoning — proofs, relations, and structures — through automated verification, aligning theoretical education with computational practice.

By transforming abstract logic into executable code, this work reinforces how discrete mathematics forms the logical backbone of algorithms, networks, cryptography, and data structures.

🏁 Future Enhancements
Interactive GUI using Tkinter for live mathematical visualization.

Symbolic proof generator for predicate logic and induction.

Graph visualizer for dynamic traversal animations.

Automated LaTeX report generation from output logs.

📜 License
This project is released for educational and academic demonstration under the MIT License.
Attribution is appreciated where reused.

🏫 Academic Integrity
All implementations were written from first principles with adherence to academic integrity.
Each module reflects both algorithmic correctness and conceptual clarity, as expected in a professional engineering submission.

“The essence of mathematics lies in its freedom.” — Georg Cantor