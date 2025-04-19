# Teaching Support Codes

This repository contains a collection of Python scripts developed to support undergraduate and postgraduate chemistry teaching, with a focus on physical chemistry concepts such as chemical kinetics and thermodynamics.

## 📂 Module: `concentration_vs_time_plots.py`

This module visualizes the concentration-time profiles of species involved in a simple consecutive reaction mechanism:

\[
\ce{A ->[k_1] X ->[k_2] Z}
\]

Both steps follow first-order kinetics, and it is assumed that only species \( A \) is present initially.

### 🔍 Features

- **Analytical solution:** Uses exact expressions for \([A](t)\), \([X](t)\), and \([Z](t)\) based on first-order rate laws.
- **User input:** Accepts multiple values of rate constants \( k_1 \) and \( k_2 \) through command line.
- **Visualization:** 
  - Plots time-dependent concentrations for the given parameters.
  - Annotates each curve for clarity.
  - Highlights the initial concentration of A with a reference line.
- **Case studies:** Supports the analysis of three kinetic scenarios:
  - \( k_1 \approx k_2 \)
  - \( k_1 \gg k_2 \)
  - \( k_1 \ll k_2 \)

### ▶️ Usage

Ensure you have `matplotlib` and `numpy` installed:

```bash
pip install matplotlib numpy
```

Then run:

```bash
python concentration_vs_time_plots.py
```

Input example when prompted:
```
Enter the values of k1 (separated by commas): 1.0, 10.0, 0.1
Enter the values of k2 (separated by commas): 1.0, 0.5, 5.0
```

### 📘 Educational Purpose

This script is intended for use in classroom demonstrations and assignments to help students understand the behavior of intermediate species in consecutive reactions and the role of relative rate constants.
