import numpy as np

# Data
logistics = np.array([59.1179, 21.7643, 19.1179])  # China, USA, Mexico
cost_0_6 = np.array([29.50, 37.88, 32.62])
cost_6p = np.array([31.97, 34.56, 33.48])
risk = np.array([37.22, 41.39, 69.67])

countries = ["China", "USA", "Mexico"]

# Try different weight combinations
print("Finding weights where Mexico wins 0-6 months, USA wins 6+ months\n")

for w_cost in np.arange(0.4, 0.7, 0.05):
    for w_risk in np.arange(0.05, 0.4, 0.05):
        w_log = 1.0 - w_cost - w_risk
        if w_log < 0 or w_log > 1:
            continue
            
        score_0_6 = w_cost * cost_0_6 + w_risk * risk + w_log * logistics
        score_6p = w_cost * cost_6p + w_risk * risk + w_log * logistics
        
        # Check if Mexico wins 0-6 (index 2) and USA wins 6+ (index 1)
        if np.argmin(score_0_6) == 2 and np.argmin(score_6p) == 1:
            print(f"FOUND: Cost={w_cost:.2f}, Risk={w_risk:.2f}, Logistics={w_log:.2f}")
            print(f"  0-6 months: China={score_0_6[0]:.2f}, USA={score_0_6[1]:.2f}, Mexico={score_0_6[2]:.2f} -> MEXICO WINS")
            print(f"  6+ months:  China={score_6p[0]:.2f}, USA={score_6p[1]:.2f}, Mexico={score_6p[2]:.2f} -> USA WINS")
            print()

