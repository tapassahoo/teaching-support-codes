import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial
from math import sqrt

# Define the radial wavefunction R_{nl}(r) for hydrogen-like atoms
def radial_wavefunction(r, n, l, Z=1):
    """
    Computes the radial wavefunction R_{nl}(r) for hydrogen-like atoms.
    """
    rho = 2 * Z * r / n
    norm_const = sqrt((2 * Z / n)**3 * factorial(n - l - 1) /
                      (2 * n * factorial(n + l)))
    laguerre_poly = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    R_nl = norm_const * np.exp(-rho / 2) * rho**l * laguerre_poly
    return R_nl

# Plotting style
plt.style.use('tableau-colorblind10')  # Replacement for seaborn-colorblind

# Quantum numbers (n, l) for states to plot
levels = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]

# Radial grid in atomic units (a.u.)
r = np.linspace(1e-5, 20, 1000)

# Color scheme
colors = plt.cm.plasma(np.linspace(0.1, 0.9, len(levels)))

# ---------- Plot 1: Radial Wavefunctions R_{nl}(r) ----------
plt.figure(figsize=(12, 7))  # Enlarged plot
for i, (n, l) in enumerate(levels):
    R = radial_wavefunction(r, n, l)
    plt.plot(r, R, color=colors[i], label=fr"$n={n},\ \ell={l}$", linewidth=2)
    max_idx = np.argmax(np.abs(R))
    plt.annotate(f"$n={n}, \\ell={l}$", xy=(r[max_idx], R[max_idx]),
                 xytext=(r[max_idx]+1, R[max_idx]+0.1),
                 arrowprops=dict(arrowstyle='->', color=colors[i]),
                 fontsize=10, color=colors[i])

plt.title(r"Radial Wavefunctions $R_{n\ell}(r)$ of Hydrogen Atom", fontsize=16)
plt.xlabel(r"Radial distance $r$ (a.u.)", fontsize=14)
plt.ylabel(r"$R_{n\ell}(r)$", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Quantum States", fontsize=11)
plt.tick_params(labelsize=12)
plt.tight_layout()
plt.show()

# ---------- Plot 2: Radial Probability Densities r^2|R_{nl}(r)|^2 ----------
plt.figure(figsize=(12, 7))  # Enlarged plot
for i, (n, l) in enumerate(levels):
    R = radial_wavefunction(r, n, l)
    prob_density = r**2 * np.abs(R)**2
    plt.plot(r, prob_density, color=colors[i], label=fr"$n={n},\ \ell={l}$", linewidth=2)
    max_idx = np.argmax(prob_density)
    plt.annotate(f"$n={n}, \\ell={l}$", xy=(r[max_idx], prob_density[max_idx]),
                 xytext=(r[max_idx]+1.2, prob_density[max_idx]+0.02),
                 arrowprops=dict(arrowstyle='->', color=colors[i]),
                 fontsize=10, color=colors[i])

plt.title(r"Radial Probability Density $r^2 |R_{n\ell}(r)|^2$", fontsize=16)
plt.xlabel(r"Radial distance $r$ (a.u.)", fontsize=14)
plt.ylabel(r"$r^2 |R_{n\ell}(r)|^2$", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Quantum States", fontsize=11)
plt.tick_params(labelsize=12)
plt.tight_layout()
plt.show()

