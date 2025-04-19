import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, e, m_e, epsilon_0

# Define the effective potential function
def V_eff(r, l):
	"""Compute the effective potential for a given r and l."""
	centrifugal = (hbar**2 * l * (l + 1)) / (2 * m_e * r**2)  # Centrifugal term
	coulomb = -e**2 / (4 * np.pi * epsilon_0 * r)  # Coulomb potential
	return centrifugal + coulomb  # Total effective potential

# Define radial range (avoiding r=0 to prevent singularity)
r_min, r_max = 0.05e-10, 5e-10  # Range in meters
r = np.linspace(r_min, r_max, 1000)

# Quantum numbers (l=0, 1, 2, 3 for comparison)
l_values = [0, 1, 2, 3]
colors = ["royalblue", "crimson", "darkgreen", "purple"]  # Colors for different l values

# Create plot
plt.figure(figsize=(9, 6), dpi=120)

for i, l in enumerate(l_values):
	plt.plot(r * 1e10, V_eff(r, l) / e, label=f"$l = {l}$", color=colors[i], linewidth=2)

	# Add annotation at different x positions to prevent overlap
	x_annotate = 1.2 + 0.6 * i  # Adjust annotation position dynamically
	y_annotate = V_eff(x_annotate * 1e-10, l) / e  # Get corresponding y-value
	plt.text(x_annotate, y_annotate, f"$l = {l}$", fontsize=12, color=colors[i],
			 bbox=dict(facecolor='white', edgecolor=colors[i], boxstyle='round,pad=0.3'))

# Formatting
plt.xlabel(r"Radial distance $r$ (Å)", fontsize=14, fontweight='bold')
plt.ylabel(r"Effective Potential $V_{\text{eff}}(r)$ (eV)", fontsize=14, fontweight='bold')
plt.title("Effective Potential of Hydrogen-like Atom", fontsize=16, fontweight='bold', color='darkblue')

# Display equation of V_eff(r)
plt.text(2.5, -15, r"$V_{\text{eff}}(r) = \frac{\hbar^2 l (l+1)}{2 m_e r^2} - \frac{e^2}{4 \pi \epsilon_0 r}$",
		 fontsize=14, color="black", bbox=dict(facecolor="lightyellow", edgecolor="black", boxstyle="round,pad=0.3"))

plt.axhline(0, color="gray", linestyle="--", linewidth=1)  # Reference line at V = 0
plt.legend(fontsize=12, loc='upper right', frameon=True, edgecolor='black')
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(-20, 10)  # Adjust y-axis for better visualization

# Save plot as a PNG file
plt.savefig("effective_potential_hydrogen_atom.png", dpi=300)

# Show plot
plt.show()

