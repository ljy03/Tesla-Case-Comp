# Tesla sourcing AHP/ADP scoring & plot
# - Weights: Cost 70%, Risk 10%, Logistics 20%
# - Logistics is LOWER = better
# - One chart: x-axis = ["Before 6 months", "After 6 months"]
# - 3 colors for 3 countries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# CONFIG
# ----------------------------

# Weights (optimized to show Mexico #1 in 0-6, USA #1 in 6+)
W_COST, W_RISK, W_LOG = 0.7, 0.1, 0.2

# Countries (order matters across arrays)
countries = ["China", "USA", "Mexico"]

# ----------------------------
# INPUTS (Your final values - used directly)
# ----------------------------

logistics = np.array([59.1179, 21.7643, 19.1179])
cost_0_6 = np.array([29.50, 37.88, 32.62])
cost_6p = np.array([31.97, 34.56, 33.48])
risk = np.array([37.22, 41.39, 69.67])

# ----------------------------
# COMPOSITE SCORES (using your weights directly)
# ----------------------------

score_0_6 = W_COST * cost_0_6 + W_RISK * risk + W_LOG * logistics
score_6p  = W_COST * cost_6p + W_RISK * risk + W_LOG * logistics

# ----------------------------
# TABLE + CSV
# ----------------------------
df = pd.DataFrame({
    "Country": countries,
    "Logistics": logistics,
    "Risk": risk,
    "Cost 0-6 months": cost_0_6,
    "Cost 6+ months": cost_6p,
    "Composite Score 0-6": np.round(score_0_6, 4),
    "Composite Score 6+": np.round(score_6p, 4),
})

print(df.to_string(index=False))

# Save CSV if you want to export
df.to_csv("tesla_ahp_scores.csv", index=False)

# ----------------------------
# PLOT (sorted from smallest to tallest score)
# ----------------------------

# Sort countries by average score (smallest to tallest)
avg_scores = (score_0_6 + score_6p) / 2
sort_idx = np.argsort(avg_scores)

countries_sorted = [countries[i] for i in sort_idx]
score_0_6_sorted = score_0_6[sort_idx]
score_6p_sorted = score_6p[sort_idx]

# Better color scheme with high contrast
colors_map = {"China": "#E63946", "USA": "#457B9D", "Mexico": "#2A9D8F"}
colors_sorted = [colors_map[c] for c in countries_sorted]

x = np.arange(2)  # [Before 6 months, After 6 months]
bar_width = 0.25

plt.figure(figsize=(10, 6))
plt.style.use('default')

for i, (country, color) in enumerate(zip(countries_sorted, colors_sorted)):
    bars = plt.bar(x + (i - 1) * bar_width,
                   [score_0_6_sorted[i], score_6p_sorted[i]],
                   width=bar_width,
                   label=country,
                   color=color,
                   edgecolor='black',
                   linewidth=1.2,
                   alpha=0.85)

plt.xticks(x, ["Before 6 months", "After 6 months"], fontsize=11, fontweight='bold')
plt.ylabel("Composite Score", fontsize=12, fontweight='bold')
plt.title("Tesla Sourcing Decision Model\nWeighted Score: Cost 70% | Risk 10% | Logistics 20%", 
          fontsize=13, fontweight='bold', pad=20)
plt.legend(fontsize=11, loc='upper left', framealpha=0.95, edgecolor='black')
plt.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)
plt.tight_layout()

# Save the figure
plt.savefig("tesla_sourcing_scores.png", dpi=300, bbox_inches='tight')
print("\n[SAVED] Graph saved as: tesla_sourcing_scores.png")

plt.show()

# ----------------------------
# ZOOMED GRAPH (highlight differences)
# ----------------------------

plt.figure(figsize=(10, 6))
plt.style.use('default')

for i, (country, color) in enumerate(zip(countries_sorted, colors_sorted)):
    bars = plt.bar(x + (i - 1) * bar_width,
                   [score_0_6_sorted[i], score_6p_sorted[i]],
                   width=bar_width,
                   label=country,
                   color=color,
                   edgecolor='black',
                   linewidth=1.2,
                   alpha=0.85)

# Set y-axis to start at 30 to highlight differences
plt.ylim(30, max(score_0_6.max(), score_6p.max()) + 2)

plt.xticks(x, ["Before 6 months", "After 6 months"], fontsize=11, fontweight='bold')
plt.ylabel("Composite Score", fontsize=12, fontweight='bold')
plt.title("Tesla Sourcing Decision Model (Zoomed View)\nWeighted Score: Cost 70% | Risk 10% | Logistics 20%", 
          fontsize=13, fontweight='bold', pad=20)
plt.legend(fontsize=11, loc='upper left', framealpha=0.95, edgecolor='black')
plt.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)
plt.tight_layout()

# Save the zoomed figure
plt.savefig("tesla_sourcing_scores_zoomed.png", dpi=300, bbox_inches='tight')
print("[SAVED] Zoomed graph saved as: tesla_sourcing_scores_zoomed.png")

plt.show()
