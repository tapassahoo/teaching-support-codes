import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, electron_mass, e, epsilon_0

# Constants
m_e = electron_mass  # Electron mass in kg

def get_l_value():
	"""Prompt user for quantum number l and validate input."""
	while True:
		try:
			l = int(input("Enter the quantum number l (integer ≥ 0): "))
			if l < 0:
				raise ValueError("Quantum number l must be a non-negative integer.")
			return l
		except ValueError as err:
			print(f"Invalid input: {err}. Please enter a valid non-negative integer.")

def compute_potential_terms(l, r):
	"""Compute centrifugal, Coulomb, and total effective potentials."""
	V_centrifugal = (hbar**2 * l * (l + 1)) / (2 * m_e * r**2)
	V_coulomb = -e**2 / (4 * np.pi * epsilon_0 * r)
	V_eff = V_centrifugal + V_coulomb

	# Convert energy to electron volts (eV)
	return V_centrifugal / e, V_coulomb / e, V_eff / e

def plot_potential(l, r_angstrom, V_centrifugal, V_coulomb, V_eff):
	"""Plot the effective potential and its components."""
	plt.figure(figsize=(9, 6), dpi=120)

	# Plot each potential term
	plt.plot(r_angstrom, V_centrifugal, label=r'Centrifugal Term', linestyle='dashed', color='royalblue', linewidth=2)
	plt.plot(r_angstrom, V_coulomb, label=r'Coulomb Term', linestyle='dotted', color='crimson', linewidth=2)
	plt.plot(r_angstrom, V_eff, label=r'Total Effective Potential', color='black', linewidth=2)

	# Annotate l value inside the plot
	plt.text(7, 3.6, f"Quantum Number $l = {l}$", fontsize=14,
			 bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.4'))

	# Formatting the plot
	plt.axhline(0, color='gray', linewidth=1, linestyle='--')
	plt.xlabel(r'Radial Distance $r$ (Å)', fontsize=14, fontweight='bold')
	plt.ylabel(r'Potential Energy $V_{\text{eff}}(r)$ (eV)', fontsize=14, fontweight='bold')
	plt.title(f'Effective Potential for $l = {l}$ in a Hydrogen-like Atom', fontsize=16, fontweight='bold', color='darkblue')

	# Enhance legend
	plt.legend(fontsize=12, loc='upper right', frameon=True, edgecolor='black')

	# Improve grid visibility
	plt.grid(True, linestyle="--", alpha=0.5)

	# Adjust y-axis limits for better visualization
	plt.ylim(-30, 50)

	# Show the plot
	plt.show()

def main():
	"""Main function to execute the workflow."""
	#l = get_l_value()  # Get user input for l

	# Define radial distance (avoiding r=0)
	r = np.linspace(0.1e-10, 10e-10, 500)  # meters
	r_angstrom = r * 1e10  # Convert meters to Ångström

	for l in range(4):
		# Compute potential terms
		V_centrifugal, V_coulomb, V_eff = compute_potential_terms(l, r)

		# Plot the results
		plot_potential(l, r_angstrom, V_centrifugal, V_coulomb, V_eff)

# Run the program
if __name__ == "__main__":
	main()

