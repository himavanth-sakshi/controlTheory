# Chapter 4: Time Response

## Overview
Chapter 4 focuses on analyzing the **time-domain response** of control systems. It introduces how systems behave over time when subjected to standard inputs (step, impulse, ramp), and how performance metrics such as **rise time**, **settling time**, and **overshoot** are used to evaluate system performance.

---

## 4.1 Standard Test Signals
Used to test and analyze system performance:
- **Step Input:** \( r(t) = A \cdot u(t) \)
- **Ramp Input:** \( r(t) = At \)
- **Impulse Input:** \( r(t) = A\delta(t) \)

These inputs help characterize dynamic system response.

---

## 4.2 First-Order System Response
Transfer function:
\[ G(s) = \frac{1}{\tau s + 1} \]

Step response:
\[ c(t) = 1 - e^{-t/\tau} \]

Where:
- \( \tau \): Time constant
- \( c(t) \): Output response

Time constant \( \tau \) indicates speed of response.

---

## 4.3 Second-Order System Response
Transfer function:
\[ G(s) = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2} \]

Where:
- \( \omega_n \): Natural frequency
- \( \zeta \): Damping ratio

### Damping Classifications:
- **Underdamped (0 < \zeta < 1)**: Oscillatory response
- **Critically damped (\zeta = 1)**: Fastest non-oscillatory
- **Overdamped (\zeta > 1)**: Slow non-oscillatory

---

## 4.4 Time-Domain Specifications
For underdamped second-order systems:

- **Rise Time (\( t_r \))**: Time to go from 10% to 90% of final value
- **Peak Time (\( t_p \))**:
  \[ t_p = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}} \]
- **Maximum Overshoot (\( M_p \))**:
  \[ M_p = e^{-\zeta \pi / \sqrt{1 - \zeta^2}} \times 100\% \]
- **Settling Time (\( t_s \))** (2% criterion):
  \[ t_s \approx \frac{4}{\zeta \omega_n} \]

---

## 4.5 Effect of Poles on Time Response
- Dominant poles near the imaginary axis cause oscillations.
- Poles farther left in the s-plane result in faster decay.
- Complex conjugate poles govern oscillatory behavior.

---

## 4.6 Time Response of Higher-Order Systems
- Approximate using **dominant poles** if other poles are far left in the s-plane.
- Higher-order systems can often be simplified to second-order equivalents.

---

## Key Equations Summary
1. \( G(s) = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2} \)
2. \( M_p = e^{-\zeta \pi / \sqrt{1 - \zeta^2}} \times 100\% \)
3. \( t_p = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}} \)
4. \( t_s = \frac{4}{\zeta \omega_n} \)
5. \( c(t) = 1 - e^{-t/\tau} \) for first-order systems

---

## Key Takeaways
- Standard time-domain inputs allow for testing transient behavior.
- Second-order systems provide insight into real-world system performance.
- Rise time, overshoot, and settling time are critical for system design.
- Pole locations dictate transient response.

---

## Next Steps
- Simulate time responses in Python/MATLAB.
- Practice identifying system parameters (\( \omega_n \), \( \zeta \)) from responses.
- Explore system tuning to meet time-domain specifications.

---

