# Chapter 2: Mathematical Models of Systems

## Overview
Chapter 2 focuses on developing **mathematical models** for different physical systems, including **mechanical, electrical, and electromechanical systems**. It introduces **differential equations, transfer functions, block diagrams, and state-space representation** to analyze system dynamics.

---

## 2.1 Mathematical Modeling of Physical Systems
A **mathematical model** represents a system’s behavior using **differential equations**, which can be converted into **transfer functions** or **state-space models** for analysis.

### Why Model Systems?
- Predict system behavior
- Design and tune controllers
- Simulate and optimize performance

---

## 2.2 Transfer Function
The **transfer function** \( G(s) \) describes the system’s input-output relationship in the **Laplace domain**.

\[ G(s) = \frac{\text{Output}}{\text{Input}} \]

- Assumes **zero initial conditions**.
- Used for **linear time-invariant (LTI) systems**.
- Provides system characteristics like **poles, zeros, and stability**.

### Example: Transfer Function of an RC Circuit
For an **RC circuit**:
\[ G(s) = \frac{1}{RCs + 1} \]

---

## 2.3 Mechanical System Modeling
Mechanical systems are modeled using **Newton’s Laws**.

### Translational System (Mass-Spring-Damper)
\[ M\ddot{x} + B\dot{x} + Kx = F(t) \]

Laplace Transform:
\[ G(s) = \frac{X(s)}{F(s)} = \frac{1}{Ms^2 + Bs + K} \]

### Rotational System (Inertia-Spring-Damper)
\[ J\ddot{\theta} + B\dot{\theta} + K\theta = T(t) \]

Laplace Transform:
\[ G(s) = \frac{\Theta(s)}{T(s)} = \frac{1}{Js^2 + Bs + K} \]

---

## 2.4 Electrical System Modeling
Using **Kirchhoff’s Laws**, electrical circuits can be modeled as differential equations.

### Series RLC Circuit
\[ L\frac{d^2i}{dt^2} + R\frac{di}{dt} + \frac{i}{C} = V(t) \]

Laplace Transform:
\[ G(s) = \frac{I(s)}{V(s)} = \frac{1}{Ls^2 + Rs + \frac{1}{C}} \]

---

## 2.5 Electromechanical Systems
Electromechanical systems involve **electrical circuits driving mechanical components**.

### DC Motor Model
- **Electrical equation:**
  \[ V_a = L_a \frac{di_a}{dt} + R_a i_a + K_b \omega \]

- **Mechanical equation:**
  \[ J \frac{d\omega}{dt} + B\omega = K_t i_a \]

Transfer function:
\[ G(s) = \frac{\Omega(s)}{V_a(s)} = \frac{K_t}{(Js + B)(L_a s + R_a) + K_b K_t} \]

---

## 2.6 Block Diagram Representation
Control systems can be represented using **block diagrams** to simplify system analysis.

### Block Diagram Reduction Rules:
1. **Cascade connection:** \( G_1(s)G_2(s) \)
2. **Parallel connection:** \( G_1(s) + G_2(s) \)
3. **Feedback loop:**
   \[ T(s) = \frac{G(s)}{1 + G(s)H(s)} \]

---

## 2.7 State-Space Representation
An alternative to transfer functions, **state-space models** represent systems as **first-order differential equations**.

- **State Equation:**
  \[ \dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t) \]

- **Output Equation:**
  \[ \mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t) \]

Example for a **mass-spring-damper** system:

\[ A = \begin{bmatrix} 0 & 1 \\ -\frac{K}{M} & -\frac{B}{M} \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ \frac{1}{M} \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad D = 0 \]

---

## Key Takeaways
- **Mathematical modeling** helps analyze system behavior.
- **Transfer functions** describe system dynamics in the **Laplace domain**.
- **Block diagrams** simplify system interconnections.
- **State-space models** provide a general framework for dynamic systems.

---

## Next Steps
- Implement numerical simulations in Python.
- Study block diagram reduction techniques.
- Understand control system stability criteria.

---

