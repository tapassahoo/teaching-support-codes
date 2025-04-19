import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial
from math import sqrt

# Radial wavefunction R_{nl}(r)
def radial_wavefunction(r, n, l, Z=1):
	rho = 2 * Z * r / n
	norm_const = sqrt((2 * Z / n)**3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
	laguerre_poly = genlaguerre(n - l - 1, 2 * l + 1)(rho)
	R_nl = norm_const * np.exp(-rho / 2) * rho**l * laguerre_poly
	return R_nl

# Find node positions: where wavefunction crosses zero
def find_nodes(r, R):
	nodes = []
	for i in range(1, len(R)):
		if R[i-1]*R[i] < 0:
			r_node = r[i-1] - R[i-1]*(r[i] - r[i-1]) / (R[i] - R[i-1])
			nodes.append(r_node)
	return nodes

# Settings
plt.style.use('seaborn-v0_8-colorblind')  # For compatibility with newer matplotlib
r = np.linspace(1e-5, 13, 1500)
levels = [(1, 0), (2, 0), (3, 0)]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, orange, green

# Plot: Radial Wavefunctions with node annotations
plt.figure(figsize=(12, 7))
for i, (n, l) in enumerate(levels):
	R = radial_wavefunction(r, n, l)
	plt.plot(r, R, color=colors[i], linewidth=2, label=fr"$n={n}, \ell={l}$")

	# Annotate peak
	peak_idx = np.argmax(np.abs(R))
	peak_r = r[peak_idx]
	peak_val = R[peak_idx]
	plt.annotate(fr"$n={n}, \ell={l}$", xy=(peak_r, peak_val),
				 xytext=(peak_r + 0.5, peak_val + 0.1),
				 fontsize=12, color=colors[i],
				 arrowprops=dict(arrowstyle='->', color=colors[i]))

	# Annotate node positions
	nodes = find_nodes(r, R)
	for j, rn in enumerate(nodes):
		plt.axvline(x=rn, color=colors[i], linestyle='--', alpha=0.5)
		plt.text(rn, 0.05 + 0.05*j, f"{rn:.2f}", rotation=90,
				 color=colors[i], fontsize=10, ha='center', va='bottom')

plt.title(r"Radial Wavefunctions $R_{n\ell}(r)$ for Hydrogen Atom", fontsize=16)
plt.xlabel(r"Radial distance $r$ (in units of $a_0$)", fontsize=14)
plt.ylabel(r"$R_{n\ell}(r)$", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.xlim(0, 13)
plt.tight_layout()
plt.show()

