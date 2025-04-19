import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial
from math import sqrt
import seaborn as sns
from scipy.optimize import brentq

# Set Seaborn style for better aesthetics
sns.set(style='whitegrid', context='notebook', palette='bright')

# Bohr radius in atomic units (a.u.)
a0 = 1

# Function to compute the radial wavefunction R_{nℓ}(r)
def radial_wavefunction(r, n, l, Z=1):
    rho = 2 * Z * r / n  # Scaled radial coordinate
    # Normalization constant
    norm_const = sqrt((2 * Z / n)**3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
    # Associated Laguerre polynomial
    laguerre_poly = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    # Radial wavefunction expression
    R_nl = norm_const * np.exp(-rho / 2) * rho**l * laguerre_poly
    return R_nl

# Function to plot radial wavefunctions and radial probability densities
def plot_radial_data(n, r_max=13, Z=1):
    r = np.linspace(1e-5, r_max, 1000)  # Radial grid
    colors = sns.color_palette("tab10", n)  # Distinct colors for each ℓ

    # --- Plot Radial Wavefunctions R_{nℓ}(r) ---
    plt.figure(figsize=(10, 6))
    for l in range(n):
        R = radial_wavefunction(r, n, l, Z)  # Compute R_{nℓ}(r)
        plt.plot(r / a0, R, label=fr'$\ell={l}$', linewidth=2, color=colors[l])  # Plot line

        # Annotate curve with LaTeX label R_{n,l}(r)
        idx = int(0.8 * len(r))  # Choose a point near the right of the curve
        plt.text(
            r[idx] / a0,
            R[idx],
            fr'$R_{{{n},{l}}}(r)$',
            fontsize=12,
            color=colors[l]
        )

        # Annotate nodes (where R crosses zero)
        if n - l - 1 > 0:
            guess_r = np.linspace(1e-5, r_max, 200)
            nodes = []
            for i in range(len(guess_r) - 1):
                try:
                    root = brentq(lambda x: radial_wavefunction(x, n, l), guess_r[i], guess_r[i+1])
                    if not any(np.isclose(root, nodes, atol=1e-2)):
                        nodes.append(root)
                        plt.axvline(x=root / a0, color='gray', linestyle='--', alpha=0.6)
                        plt.text(root / a0 + 0.2, 0.02, f'{root:.2f}', fontsize=9, color='gray')
                except:
                    continue

    plt.title(fr'Radial Wavefunctions $R_{{n\ell}}(r)$ for $n={n}$', fontsize=15)
    plt.xlabel(r'Radial distance $r / a_0$', fontsize=13)
    plt.ylabel(r'$R_{n\ell}(r)$', fontsize=13)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- Plot Radial Probability Densities r²|R_{nℓ}(r)|² ---
    plt.figure(figsize=(10, 6))
    for l in range(n):
        R = radial_wavefunction(r, n, l, Z)
        prob_density = r**2 * np.abs(R)**2  # Radial probability density
        plt.plot(r / a0, prob_density, label=fr'$\ell={l}$', linewidth=2, color=colors[l])

        # Optional annotation (similar to R_{nℓ}) can be added here if needed
        idx = np.argmax(prob_density)
        plt.text(
            r[idx] / a0,
            prob_density[idx],
            fr'$r^2|R_{{{n},{l}}}(r)|^2$',
            fontsize=12,
            color=colors[l]
        )

    plt.title(fr'Radial Probability Densities $r^2 |R_{{n\ell}}(r)|^2$ for $n={n}$', fontsize=15)
    plt.xlabel(r'Radial distance $r / a_0$', fontsize=13)
    plt.ylabel(r'$r^2 |R_{n\ell}(r)|^2$', fontsize=13)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage for hydrogen atom with n=3
plot_radial_data(n=3, r_max=20)

