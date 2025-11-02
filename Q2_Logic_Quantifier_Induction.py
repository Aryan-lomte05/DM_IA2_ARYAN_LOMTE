# Q2_PredicateLogic_Induction.py
"""
Q2: Predicate Logic + Mathematical Induction Verifier
----------------------------------------------------
Part A: Evaluate quantified statements (∀, ∃) over finite domains.
Part B: Verify a mathematical induction formula numerically.
"""

import sympy as sp
import os

# ---------- File Setup ----------
output_path = r"C:\Users\Aryan\DM_IA2_ARYAN_LOMTE\outputs\Q2_output.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
open(output_path, "w").close()

def log_output(text):
    print(text)
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

log_output("=== Q2: Predicate Logic + Mathematical Induction Verifier ===\n")

# ---------- PART A: Quantified Predicate Evaluation ----------
def evaluate_quantified(statement, domain):
    x, y = sp.symbols('x y', integer=True)
    results = []

    for_all = 'forall' in statement
    exists = 'exists' in statement

    if for_all and exists:
        predicate = statement.split('(')[-1].split(')')[0].strip()
        log_output(f"Evaluating: ∀x ∃y ({predicate}) over domain {domain}")
        for xv in domain:
            exists_y = any(eval(predicate.replace('x', str(xv)).replace('y', str(yv))) for yv in domain)
            results.append(exists_y)
            log_output(f"For x={xv}, ∃y → {exists_y}")
        log_output("Final Result: " + ("True ✅" if all(results) else "False ❌"))
    else:
        log_output("Only ∀∃ pattern supported in this demo.")

# ---------- PART B: Mathematical Induction Verification ----------
def verify_induction(limit_n=10):
    n = sp.Symbol('n', integer=True, positive=True)
    log_output("\nVerifying Induction Formula:")
    log_output("Σ(n²) = n(n+1)(2n+1)/6\n")
    for k in range(1, limit_n + 1):
        lhs_val = sum(i**2 for i in range(1, k+1))
        rhs_val = (k*(k+1)*(2*k+1))//6
        status = "OK ✅" if lhs_val == rhs_val else "FAIL ❌"
        log_output(f"n={k}: LHS={lhs_val}, RHS={rhs_val} → {status}")

# ---------- Execution ----------
domain = list(range(1, 5))
evaluate_quantified("forall x exists y (x < y)", domain)
verify_induction(10)

log_output("\n✅ Output successfully saved to Q2_output.txt")
