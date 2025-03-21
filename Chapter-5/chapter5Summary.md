# Chapter 5: Reduction of Multiple Subsystems

## Overview
Chapter 5 introduces methods for reducing **complex block diagrams** and **signal flow graphs** into simplified forms. This is essential for analyzing and designing control systems effectively.

---

## 5.1 Block Diagram Algebra
A **block diagram** represents a system with blocks (transfer functions) and signal paths.

### Common Operations:
- **Cascade (Series) Connection:**
  \[ T(s) = G_1(s) \cdot G_2(s) \]
- **Parallel Connection:**
  \[ T(s) = G_1(s) + G_2(s) \]
- **Feedback Connection:**
  - Negative feedback:
    \[ T(s) = \frac{G(s)}{1 + G(s)H(s)} \]

---

## 5.2 Block Diagram Reduction Rules
To simplify complex diagrams:
1. Combine series blocks.
2. Combine parallel blocks.
3. Move summing points and take-off points.
4. Reduce inner feedback loops first.
5. Work from inner to outer loops.

**Tip:** Redraw the diagram step-by-step to track simplifications.

---

## 5.3 Signal Flow Graphs (SFGs)
A **Signal Flow Graph (SFG)** is a graphical representation of a set of linear algebraic equations.
- **Nodes:** Represent variables
- **Branches:** Represent gains

---

## 5.4 Mason's Gain Formula
Used to calculate the overall transfer function from a signal flow graph.

\[ T = \frac{\sum_{k=1}^{N} P_k \Delta_k}{\Delta} \]

Where:
- \( P_k \): Gain of the k-th forward path
- \( \Delta \): Determinant of the graph (1 - sum of individual loop gains + sum of gain products of non-touching loops - ...)
- \( \Delta_k \): Value of \( \Delta \) with loops touching \( P_k \) removed

---

## 5.5 Example: Feedback System Reduction
Given:
\[ G(s) = \frac{10}{s+5}, \quad H(s) = \frac{1}{s+2} \]

Feedback connection:
\[ T(s) = \frac{G(s)}{1 + G(s)H(s)} = \frac{10}{(s+5) + \frac{10}{s+2}} \]

---

## Key Takeaways
- Use block diagram algebra to simplify complex systems step-by-step.
- Mason’s Gain Formula offers a powerful method for signal flow analysis.
- Always reduce **inner loops** before outer loops.

---

## Next Steps
- Practice reducing diagrams with multiple loops.
- Learn to convert between block diagrams and signal flow graphs.
- Use Python/MATLAB to simulate and validate results.

---

