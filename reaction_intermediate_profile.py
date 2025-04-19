import numpy as np
import matplotlib.pyplot as plt

def plot_exponential_difference(k1, k2, t_max=None):
    """
    Plots exp(-k1 * t), exp(-k2 * t), and their difference.
    
    Parameters:
        k1 (float): Rate constant 1 (s⁻¹)
        k2 (float): Rate constant 2 (s⁻¹)
        t_max (float, optional): Maximum time for plotting (s). 
                                 Automatically set based on smaller rate constant if not given.
    """
    # Set default t_max based on slower rate
    if t_max is None:
        t_max = 10e-3/ min(k1, k2)
        #t_max = 1/ min(k1, k2)
    
    # Time array
    t = np.linspace(0, t_max, 1000)

    # Exponential terms
    exp_k1 = np.exp(-k1 * t)
    exp_k2 = np.exp(-k2 * t)
    difference = exp_k1 - exp_k2

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t, exp_k1, label=fr'$e^{{-k_1 t}},\ k_1 = {k1}\ \mathrm{{s^{{-1}}}}$', linestyle='--', color='tab:blue')
    plt.plot(t, exp_k2, label=fr'$e^{{-k_2 t}},\ k_2 = {k2}\ \mathrm{{s^{{-1}}}}$', linestyle='--', color='tab:orange')
    plt.plot(t, difference, label=r'$e^{-k_1 t} - e^{-k_2 t}$', linewidth=2, color='tab:green')

    # Annotate peak of the difference
    peak_idx = np.argmax(difference)
    plt.annotate('Peak of intermediate',
                 xy=(t[peak_idx], difference[peak_idx]),
                 xytext=(t[peak_idx] + 0.05 * t_max, difference[peak_idx] + 0.05),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10)

    # Display rate constants
    rate_text = fr'$k_1 = {k1}\ \mathrm{{s^{{-1}}}},\ k_2 = {k2}\ \mathrm{{s^{{-1}}}}$'
    plt.text(0.7 * t_max, 0.85, rate_text, fontsize=11, bbox=dict(facecolor='whitesmoke', edgecolor='gray'))

    # Labels and formatting
    plt.xlabel('Time (t)', fontsize=12)
    plt.ylabel('Function Value', fontsize=12)
    plt.title(r'Decay Curves and Intermediate Term ($k_2 \neq k_1$)', fontsize=14)
    plt.grid(True, linestyle=':')
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()

# Example usage
plot_exponential_difference(k1=10e-3, k2=100)
plot_exponential_difference(k1=10e-2, k2=1000)
plot_exponential_difference(k1=10e-1, k2=10000)
plot_exponential_difference(k1=10, k2=100000)
plot_exponential_difference(k1=100, k2=1000000)

