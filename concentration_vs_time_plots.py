def conc_profiles(t, A0, k1, k2):
    A = A0 * np.exp(-k1 * t)
    if abs(k1 - k2) < 1e-6:
        X = k1 * t * np.exp(-k1 * t) * A0
        Z = A0 * (1 - (1 + k1 * t) * np.exp(-k1 * t))
    else:
        X = (k1 * A0 / (k2 - k1)) * (np.exp(-k1 * t) - np.exp(-k2 * t))
        Z = A0 * (1 - (k2 * np.exp(-k1 * t) - k1 * np.exp(-k2 * t)) / (k2 - k1))
    return A, X, Z

# User input with validation
try:
    A0 = float(input("Enter initial concentration of A (A0 > 0): "))
    k1 = float(input("Enter rate constant k1 (> 0): "))
    k2 = float(input("Enter rate constant k2 (> 0): "))

    if A0 <= 0 or k1 <= 0 or k2 <= 0:
        raise ValueError("All values must be positive.")

except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Time array
t = np.linspace(0, 40, 500)

# Compute concentration profiles
A, X, Z = conc_profiles(t, A0, k1, k2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, A, label='[A](t)', color='blue')
plt.plot(t, X, label='[X](t)', color='orange')
plt.plot(t, Z, label='[Z](t)', color='green')

# Add horizontal line for A0
plt.axhline(y=A0, color='gray', linestyle='--', linewidth=1, label='[A]₀')

# Annotate each curve at suitable positions
plt.text(t[-1], A[-1], ' [A](t)', color='blue', va='center')
plt.text(t[np.argmax(X)], X.max(), ' [X](t)', color='orange', va='bottom')
plt.text(t[-1], Z[-1], ' [Z](t)', color='green', va='center')

# Labels and title
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title(f'Concentration vs Time\n(k₁={k1}, k₂={k2}, [A]₀={A0})')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()

