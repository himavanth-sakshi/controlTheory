# Chapter 2: Mathematical Models of Systems

## Overview
Chapter 2 focuses on developing **mathematical models** for different physical systems, including **mechanical, electrical, and electromechanical systems**. It introduces **differential equations, transfer functions, block diagrams, and state-space representation** to analyze system dynamics.

---

## 2.1 Mathematical Modeling of Physical Systems
A **mathematical model** represents a system’s behavior using **differential equations**, which can be converted into **transfer functions** or **state-space models** for analysis.

**Two ways of developing mathematical models**
1. Transfer functions in frequency domain
2. state equations in time domain

**NOTE** : necessary assumptions have to be made to create a mathematical model. 

### Why Model Systems?
- Predict system behavior
- Design and tune controllers
- Simulate and optimize performance

---

## 2.2 Transfer Function

It is difficult to model a system represented by differential equations --> So need for **Laplace transformation.**

The Laplace transform of a function \( f(t) \) is defined as:

$$\mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) \.dt$$





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
## 2.9 Electric Circuit Analogs
This section explains how mechanical systems can be represented by equivalent electrical circuits, highlighting the deep mathematical similarity between them. This approach helps simplify problem-solving by converting mechanical motion problems into electrical network problems.

**Electrical Circuit Analog:**
An electric circuit analog is an electrical network whose equations behave like those of a mechanical system.
This is based on the mathematical similarity between Kirchhoff's laws (for electrical systems) and Newton's laws (for mechanical systems).

**Why Use Analogs?**
Translating mechanical problems into electric circuit equivalents can simplify modeling and analysis.
The variables in the electrical circuits (e.g., current, voltage) map directly to mechanical variables (e.g., velocity, force).

### 2.9.1 Types of Analogs

1. Series Analog (Impedance Approach):
- Based on mesh (loop) equations in electric circuits.
- Mechanical elements correspond to electrical elements as follows:

Mass M → Inductor L
Damping f_v → Resistor R
Spring K → Capacitor C

Mechanical equation of motion
$$(Ms^2 + f_v s + K)X(s) = F(s)$$

After converting displacement X(s) to velocity V(s):

$$(Ms + f_v + \frac{K}{s})V(s) = F(s)$$

Electrical Series RLC Mesh Equation:

$$(Ls + R + \frac{1}{Cs})I(s) = E(s)$$

## 2.10 NonLineraties 
The models developed so far assume linear, time-invariant differential equations, but many real-world systems are nonlinear. 

### 2.10.1 **Definition of Linearity:** A system is linear if it satisfies:
- Superposition: The response to multiple inputs is the sum of individual responses.
- Homogeneity: Scaling an input scales the output by the same factor.

### 2.10.2 **Examples of Nonlinear Systems:**
If an input x results in an output 0.5x , then:
Input = 1 → Output = 0.5
Input = 2 → Output = 1
Input = 3 (sum of 1 & 2) → Output = 1.5 (sum of 0.5 & 1)

### 2.10.3 **Example of a Linear System:**
- Saturation: Electronic amplifiers behave linearly only within a specific range.
- Dead Zone: Motors may not respond at low voltages due to friction.
- Backlash: Gears may have loose movement, causing an input delay.
- Phase Detector: Output is the sine of the input, making it inherently nonlinear.

### 2.10.4 **Linear Approximations of Nonlinear Systems:**
- Nonlinear systems can often be approximated as linear for analysis.
- If input variations are small, a linear relationship can be assumed around a specific point.
- Example: Electronic amplifiers are approximately linear for small input changes.
---
## 2.11 Linearization

### 2.11.1 **Why Linearization is Needed?**
Many electrical and mechanical systems contain nonlinear components.
Transfer functions only apply to linear systems, so we must linearize nonlinear systems first.

### 2.11.2 Linearization Process:
Step 1: Identify the nonlinear component and write the nonlinear differential equation.
Step 2: Determine the steady-state equilibrium point where small-signal input = 0.
Step 3: Use Taylor Series Expansion to approximate the nonlinear function.
Step 4: Neglect higher-order terms to get a linear equation.
Step 5: Take the Laplace transform, assuming zero initial conditions.
Step 6: Express the system as a transfer function.

### 2.11.3 Mathematical Linearization (Using Taylor Series Approximation):
- the functionf(x) around point x_0 is approximated as:
$$f(x) \approx f(x_0) + \frac{df}{dx} \Big|_{x = x_0} (x - x_0)$$

- $$ \text{Higher-order terms } \left( \frac{d^2f}{dx^2}, \frac{d^3f}{dx^3}, \ldots \right) \text{ are ignored for small variations.} $$

### 2.11.4 Example of Linearization of pendulum equation

The equation of motion for a pendulum is:

$$M L^2 \ddot{\theta} + B \dot{\theta} + M g L \sin{\theta} = 0$$

For small angles (\( \theta \approx 0 \)), we approximate:

$$\sin{\theta} \approx \theta$$

The linearized equation becomes:

$$M L^2 \ddot{\theta} + B \dot{\theta} + M g L \theta = 0$$

This is now a linear system that can be analyzed using transfer functions.




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

