# Piecewise-constant plot: cost stays flat for first 6 months, then drops suddenly at month 6
import numpy as np
import matplotlib.pyplot as plt

# Baseline totals (USD per unit before yield effects)
total_US, total_MX, total_CN = 80.0, 77.5, 74.0

# Initial yields (constant during first 6 months), jump to 100% at month 6
y0_US, y0_MX, y0_CN = 0.80, 0.90, 0.95  # change here if you want a different pre-6m yield

# Time axis
months = np.linspace(0, 7, 71)

# Piecewise-constant yields
yield_US = np.where(months < 6, y0_US, 1.0)
yield_MX = np.where(months < 6, y0_MX, 1.0)
yield_CN = np.where(months < 6, y0_CN, 1.0)

# Corresponding price per good unit
price_US = total_US / yield_US
price_MX = total_MX / yield_MX
price_CN = total_CN / yield_CN

# Plot
plt.figure()
plt.step(months, price_US, where="post", label="US")
plt.step(months, price_MX, where="post", label="Mexico")
plt.step(months, price_CN, where="post", label="China")

plt.axvline(6, linestyle="--", linewidth=1)
plt.title("Per-lamp cost: piecewise constant with sudden drop at month 6")
plt.xlabel("Time (months)")
plt.ylabel("Price per lamp (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
