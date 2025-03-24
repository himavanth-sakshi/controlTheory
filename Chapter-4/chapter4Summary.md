# Chapter 4: Time Response

## 4.1 Overview
Chapter 4 focuses on analyzing the **time-domain response** of control systems. It introduces how systems behave over time when subjected to standard inputs (step, impulse, ramp), and how performance metrics such as **rise time**, **settling time**, and **overshoot** are used to evaluate system performance.

---
## 4.2 Poles, Zeros and System Response

The output of a system is sum of two responses
- Forced response (due to external inputs)
- Natural response (due to the system’s inherent dynamics)

While solving differential equations or taking inverse Laplace transforms can give accurate results, these methods are often time-consuming. Instead, engineers use qualitative techniques—like pole-zero analysis—for faster insight into system behavior.

## 4.2.1 **Poles of a Transfer Functions**
Poles are fundamental in understanding how a system behaves over time. They determine the stability, speed of response, and oscillatory nature of the system.

A pole of a transfer function is:
- A value of the Laplace variable s that makes the denominator of the transfer function zero, causing the function to go to infinity.
if $$G(s) = \frac{N(s)}{D(s)}$$ , then poles are the roots of D(s) = 0
- In practical control system analysis, poles also include common roots with the numerator (even if they cancel out), because they still influence the system behavior.

**Interpretation of Poles**
- Poles on the left-half of the s-plane → Stable system
- Poles on the right-half of the s-plane → Unstable system
- Poles on the imaginary axis → Marginally stable (e.g., pure oscillation)

**Effect of Poles on System Response**
- Real negative poles: Exponential decay (stable, slow or fast depending on magnitude)
- Complex conjugate poles: Oscillatory response
- Poles closer to origin: Slower response
- Poles farther left: Faster response
- Repeated poles: Slower settling time and can increase overshoot

## 4.2.2 **Zeros of a Transfer Functions**
Zeros play a key role in shaping how the input signal influences the output of a system. While poles govern the system’s inherent behavior (natural response), zeros affect the forced response and the shape of the output.

A zero of a transfer function is:
- A value of the Laplace variable s that makes the numerator of the transfer function equal to zero, causing the overall transfer function output to be zero.
- if $$G(s) = \frac{N(s)}{D(s)}$$ , then poles are the roots of D(s) = 0, then zeros are the roots of N(s)=0
- In practice, even if a zero cancels with a matching pole in the denominator, it's still often considered a zero, since it can still impact system behavior.

**Impact of Zeros on System Response**
- Zeros shape the output by affecting amplitude and response time.
- Real negative zeros can reduce overshoot and settle the response faster.
- Right-half-plane zeros (positive real) cause non-minimum phase behavior, leading to:
  - Initial output movement in the opposite direction (inverse response)
  - Slower rise time and more complexity in control
- Zeros near the origin tend to increase response speed, while those far from the origin may slow it down or distort it.

**Why Zeros Matter**
- Zeros influence how input signals are filtered by the system.
- Essential for shaping the time-domain response, especially in controller design.
- Help determine the location and nature of peaks in the frequency response (e.g., resonance).

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

