import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial
from math import sqrt

# Define the radial wavefunction R_{nl}(r)
def radial_wavefunction(r, n, l, Z=1):
	rho = 2 * Z * r / n
	norm_const = sqrt((2 * Z / n)**3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
	laguerre_poly = genlaguerre(n - l - 1, 2 * l + 1)(rho)
	return norm_const * np.exp(-rho / 2) * rho**l * laguerre_poly

# Generate smooth radial grid (in units of a₀)
r = np.linspace(1e-5, 100, 12000)

# Quantum states (n, l) to be plotted
states = [(1, 0), (2, 0), (3, 0)]
colors = ['#d62728', '#1f77b4', '#2ca02c']  # vibrant red, blue, green

# ------------- PLOT 1: Radial Wavefunctions -------------
plt.figure(figsize=(10, 6))

for idx, (n, l) in enumerate(states):
	R = radial_wavefunction(r, n, l)
	color = colors[idx]
	label = fr"$n={n},\ \ell={l}$"

	# Plot R_{nl}(r)
	plt.plot(r, R, color=color, lw=2, label=label)

	# Annotate peak
	r_peak = r[np.argmax(np.abs(R))]
	R_peak = R[np.argmax(np.abs(R))]
	plt.annotate(label,
				 xy=(r_peak, R_peak),
				 xytext=(r_peak + 0.5, R_peak + 0.15),
				 fontsize=12, color=color,
				 arrowprops=dict(arrowstyle='->', color=color, lw=1))

	# Annotate node positions
	num_nodes = n - l - 1
	if num_nodes > 0:
		sign_changes = np.where(np.diff(np.sign(R)))[0]
		for node_idx in sign_changes:
			node_r = r[node_idx]
			plt.axvline(node_r, color=color, linestyle='--', lw=1.2, alpha=0.5)
			plt.text(node_r, 0.05, f"{node_r:.2f}", rotation=90,
					 fontsize=9, color=color, ha='center', va='bottom')

plt.title(r"Radial Wavefunctions $R_{n\ell}(r)$ of Hydrogen Atom", fontsize=15)
plt.xlabel(r"Radial distance $r/a_0$", fontsize=13)
plt.ylabel(r"$R_{n\ell}(r)$", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.xlim(0, 13)
plt.tight_layout()
plt.savefig("radial_wavefunctions.png", dpi=400)
plt.show()


# ------------- PLOT 2: Radial Probability Density -------------
plt.figure(figsize=(10, 6))

for idx, (n, l) in enumerate(states):
	R = radial_wavefunction(r, n, l)
	P = r**2 * R**2
	color = colors[idx]
	label = fr"$n={n},\ \ell={l}$"

	# Plot radial probability density
	plt.plot(r, P, color=color, lw=2, label=label)

	# Annotate maxima of probability
	max_r = r[np.argmax(P)]
	max_val = np.max(P)
	plt.annotate(label,
				 xy=(max_r, max_val),
				 xytext=(max_r + 0.5, max_val + 0.1),
				 fontsize=12, color=color,
				 arrowprops=dict(arrowstyle='->', color=color, lw=1))

plt.title(r"Radial Probability Densities $r^2|R_{n\ell}(r)|^2$", fontsize=15)
plt.xlabel(r"Radial distance $r/a_0$", fontsize=13)
plt.ylabel(r"$r^2 |R_{n\ell}(r)|^2$", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.xlim(0, 22)
plt.tight_layout()
plt.savefig("radial_probability_density.png", dpi=400)
plt.show()

