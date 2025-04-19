import numpy as np
import pandas as pd

# Generate a fine grid of 1000 theta values from 0 to pi
theta = np.linspace(0, np.pi, 1000)
z = np.cos(theta)

# Save to a DataFrame
df = pd.DataFrame({
    'theta (rad)': theta,
    'cos(theta)': z
})

# Export to CSV if needed
df.to_csv('cos_theta_fine_grid.csv', index=False)

# Optional: Print first few rows
print(df.head())

