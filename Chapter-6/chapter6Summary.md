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

![Routh-Hurwitz Stability Criterion Table](pictureAssets/pictureAssets/6.2RouthTable.png)

**The Routh-Hurwitz criterion declares that the number of roots of the polynomial that are in the right half-plane is equal to the number of sign changes in the first column.**


- Construct a Routh Table from the characteristic polynomial.
- Interpret the table to count the number of poles in each region of the s-plane.


### Why Use Routh-Hurwitz Today?
While modern tools can compute pole locations directly, Routh-Hurwitz:
- Is efficient for design, especially when parameters are unknown.
- Helps determine stability range of an unknown parameter algebraically.
- Avoids trial-and-error approaches.

---

## 6.3 Routh-Hurwitz Criterion: Special Cases
Two special cases can occur:
1. The Routh table sometimes will have a zero only in the first column of a row 
2. the Routh table sometimes will have an entire row that consists of zeros. 


### Zero only in 1st column: 
- If the first element of a row is zero, computing the next row would cause division by zero.
- To avoid this, we replace the zero with a small positive or negative number, called epsilon (ϵ).
- After forming the rest of the table, we let ϵ approach zero and observe the signs in the first column.
- This method helps continue the Routh table construction without mathematical errors and allows determining stability.


### Entire row that consists of zeros: 

**Quick Summary: Entire Row of Zeros in Routh Table**

- Happens when the characteristic polynomial has a purely even or odd factor.
- Indicates symmetric roots about the origin — may include imaginary-axis (jω) roots.
- The row above the zero row contains this even/odd polynomial.


**How to Analyze:**
- Use the even polynomial from the row above to continue the table.
- Count sign changes from its row to the bottom → tells right-half-plane (RHP) roots.
- Due to symmetry, it has equal number of LHP and RHP roots; leftover roots lie on jω-axis.


**Key Insight:**
- A row of all zeros must be handled differently than just a single zero in a row.
- It confirms the presence of imaginary-axis roots, which are critical for determining marginal stability.


---

## 6.4 Routh-Hurwitz Criterion: Additional Examples

check the book for all examples 


---

## 6.5 Stability in State Space


### 6.5.1. State-Space vs. s-Plane Stability

- Stability can be evaluated using the **system matrix \( A \)** in state-space form.
- The **eigenvalues of \( A \)** are **equal to the poles** of the system's transfer function.


### 6.5.2. Key Equation (Eigenvalue Calculation)

Eigenvalues \( \lambda \) are found by solving:

\[\det(\lambda I - A) = 0\]

This is the **characteristic equation**, and it is the same equation used to find poles.


### 6.5.3. Relation to Transfer Function

The system transfer function is:

\[G(s) = C(sI - A)^{-1}B + D\]

Its denominator includes \( \det(sI - A) \), so solving:

\[\det(sI - A) = 0\]

yields the system's **poles** (which are also the eigenvalues of \( A \)).



### 6.5.4. Why This Is Useful

- Stability can be determined **directly from the state-space equations**.
- If \( \det(sI - A) \) is a high-degree polynomial, use the **Routh-Hurwitz criterion** to find how many eigenvalues are in each s-plane region.

---

### 6.5.5. Stability Conditions (State-Space View)

A system is **stable** if:
- All eigenvalues of \( A \) lie in the **left-half of the s-plane**.
- There are **no repeated eigenvalues on the imaginary axis (jω)**.

---

### 6.5.6. Final Conclusion

- The **eigenvalues of \( A \)** determine system stability.
- This provides a **direct and efficient method** to assess feedback system stability without converting to a transfer function.

---