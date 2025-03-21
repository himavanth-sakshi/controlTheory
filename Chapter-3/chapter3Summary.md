# Chapter 3: State-Space Representation

## Overview
Chapter 3 introduces the **state-space method** of modeling dynamic systems. Unlike transfer functions (which focus on input-output behavior), state-space models represent systems using **a set of first-order differential equations**, which makes them ideal for **multi-input multi-output (MIMO)** systems and systems with internal states.

---

## 3.1 State Variables and the State-Space Representation
A **state variable** describes the status of a system at any time. State-space models use vectors to describe system dynamics.

### General Form:
- **State Equation:**
  \[ \dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t) \]

- **Output Equation:**
  \[ \mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t) \]

Where:
- \( \mathbf{x}(t) \): State vector (n x 1)
- \( \mathbf{u}(t) \): Input vector (r x 1)
- \( \mathbf{y}(t) \): Output vector (m x 1)
- \( A \): System matrix (n x n)
- \( B \): Input matrix (n x r)
- \( C \): Output matrix (m x n)
- \( D \): Feedthrough (m x r)

---

## 3.2 Converting Differential Equations to State-Space Form
For an nth-order differential equation:

\[ a_n \frac{d^n y}{dt^n} + a_{n-1}\frac{d^{n-1}y}{dt^{n-1}} + ... + a_1\frac{dy}{dt} + a_0 y = bu \]

Define:
\[ x_1 = y, \quad x_2 = \dot{y}, \quad x_3 = \ddot{y}, \dots, \quad x_n = y^{(n-1)} \]

State equations:
\[
\dot{x}_1 = x_2 \\
\dot{x}_2 = x_3 \\
... \\
\dot{x}_n = -a_0 x_1 - a_1 x_2 - ... - a_{n-1} x_n + bu
\]

Output: \( y = x_1 \)

---

## 3.3 Converting Transfer Functions to State-Space Form
Given a transfer function:
\[ G(s) = \frac{Y(s)}{U(s)} = \frac{b_0 s^{n-1} + \dots + b_{n-1}}{s^n + a_{n-1}s^{n-1} + \dots + a_0} \]

Use **controllable canonical form**:
- A matrix: Companion matrix of denominator
- B matrix: Column vector with 1 in last row
- C matrix: Row vector of numerator coefficients
- D matrix: Usually zero (if proper TF)

---

## 3.4 Solving the State Equation
The solution of the state equation is:
\[ \mathbf{x}(t) = e^{At}\mathbf{x}(0) + \int_0^t e^{A(t-\tau)}B\mathbf{u}(\tau) d\tau \]

Where:
- \( e^{At} \): Matrix exponential (computed using series expansion or numerically)

---

## 3.5 Advantages of State-Space Representation
- Applicable to **MIMO systems**
- Describes **internal system behavior**
- Easily handles **initial conditions**
- Suitable for **digital control and simulation**

---

## Example: Mass-Spring-Damper System in State Space
\[ M\ddot{x} + B\dot{x} + Kx = F(t) \]
Let:
- \( x_1 = x \)
- \( x_2 = \dot{x} \)

Then:
- \( \dot{x}_1 = x_2 \)
- \( \dot{x}_2 = \frac{1}{M}(F - Bx_2 - Kx_1) \)

So:
\[ A = \begin{bmatrix} 0 & 1 \\ -\frac{K}{M} & -\frac{B}{M} \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ \frac{1}{M} \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad D = [0] \]

---

## Key Takeaways
- State-space models generalize dynamic systems to **vector-matrix form**.
- Useful for **higher-order** and **multi-variable** systems.
- Enables both **time-domain simulation** and **controller design**.

---

## Next Steps
- Learn how to simulate state-space systems in Python/MATLAB.
- Practice converting differential equations and transfer functions to state-space.
- Explore observability and controllability (in later chapters).

---

