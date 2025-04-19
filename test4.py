import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_p_orbital(axis='z'):
	# Define angles
	theta = np.linspace(0, np.pi, 200)
	phi = np.linspace(0, 2 * np.pi, 200)
	theta, phi = np.meshgrid(theta, phi)

	# Choose orbital based on axis
	if axis == 'z':
		Y = np.cos(theta)
		title = "p\u2093 Orbital (Dumbbell Along z-axis)"
	elif axis == 'x':
		Y = np.sin(theta) * np.cos(phi)
		title = "p\u2090 Orbital (Dumbbell Along x-axis)"
	elif axis == 'y':
		Y = np.sin(theta) * np.sin(phi)
		title = "p\u2091 Orbital (Dumbbell Along y-axis)"
	else:
		raise ValueError("Axis must be 'x', 'y', or 'z'")

	r = np.abs(Y)
	color_data = Y

	# Convert to Cartesian coordinates
	x = r * np.sin(theta) * np.cos(phi)
	y = r * np.sin(theta) * np.sin(phi)
	z = r * np.cos(theta)
	print(z)

	# Plotting
	fig = plt.figure(figsize=(8, 6))
	ax = fig.add_subplot(111, projection='3d')
	colors = plt.cm.seismic((color_data + 1) / 2)

	ax.plot_surface(x, y, z, facecolors=colors,
					rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)

	ax.set_title(title)
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	ax.set_box_aspect([1, 1, 1])
	plt.tight_layout()
	plt.show()

# Example usage:
plot_p_orbital('z')  # Change to 'x' or 'y' for other orbitals

