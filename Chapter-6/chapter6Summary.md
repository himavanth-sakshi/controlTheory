# Chapter 6: Stability

## Overview
Chapter 5 introduces methods for reducing **complex block diagrams** and **signal flow graphs** into simplified forms. This is essential for analyzing and designing control systems effectively.

---

## 6.1 Introduction 

Three requirements enter into the design of a control system:
- transient response, 
- stability ( most important), and 
- steady-state errors

Without stability both transient response and steady state errors are waste of time. 

Total response of a system is the sum of the forced and natural responses. 
**c(t) = c_forced(t) + c_natural(f)** 



**Definitions of Stability for a linear, time-invariant system**
-  stable -->  the natural response approaches zero as time approaches infinity.
- unstable if the natural response grows without bound as time approaches infinity.
- marginally stable if the natural response neither decays nor grows but remains constant or oscillates as time approaches infinity.

- the above depends on Natural Response but In practice, it's hard to separate the natural and forced responses when observing the total system response.

**Alternative Definition for Stability:**
- A system is stable if every bounded input yields a bounded output. This is known as the Bounded-Input, Bounded-Output (BIBO) Stability criterion.
- If the input is bounded and the output remains bounded, the system is considered stable.
- If the input is unbounded, and the output also grows without bound, we cannot determine stability since the growth may be due to either the forced or natural response.

### How to determine stability based on poles: 
- A stable system has all closed-loop poles in the left-half s-plane.
- An unstable system has at least one pole in the right-half plane or multiple poles on the imaginary axis.
- A marginally stable system has only simple (multiplicity = 1) poles on the imaginary axis and the rest in the LHP.

---

## 6.2 Routh-Hurwitz Stability Criterion 

solving poles could be hard --> The Routh-Hurwitz criterion helps determine system stability without solving for the exact pole locations.

It tells how many closed-loop poles lie in:(But not their exact coordinates)
- The left-half plane (LHP)
- The right-half plane (RHP)
- On the imaginary axis

![Routh-Hurwitz Stability Criterion Table](pictureAssets/6.2RouthTable.png)

### Method Overview:
- Construct a Routh Table from the characteristic polynomial.
- Interpret the table to count the number of poles in each region of the s-plane.


### Why Use Routh-Hurwitz Today?
While modern tools can compute pole locations directly, Routh-Hurwitz:
- Is efficient for design, especially when parameters are unknown.
- Helps determine stability range of an unknown parameter algebraically.
- Avoids trial-and-error approaches.








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

