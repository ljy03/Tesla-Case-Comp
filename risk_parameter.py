import numpy as np
import math
from collections import OrderedDict

def logistic_scores(x, center=None, T=None):
    x = np.asarray(x, dtype=float)
    mu = np.mean(x) if center is None else float(center)
    s = np.std(x, ddof=1) if T is None else float(T)
    if s == 0:
        s = 1e-9  # 防除零；所有数相同则整列会得到同一分
    z = (x - mu) / s
    scores = 100.0 / (1.0 + np.exp(-z))
    return scores

# ---------------- 输入（按“中/美/墨”的顺序） ----------------
countries = ["China", "USA", "Mexico"]

# 损坏率（%）
damage_pct = np.array([7.6609, 1.4970, 0.4561], dtype=float)

# 对 USD 的汇率波动率（%）：CNY, USD(=0), MXN
fxvol_pct = np.array([4.48, 0.0, 12.94], dtype=float)

# 加权系数
w_damage = 0.8
w_fx = 0.2

# -------------- 计算（logistic 归一化 × 100） --------------
damage_scores = logistic_scores(damage_pct)        # 越小越好 => 分数越低
fx_scores     = logistic_scores(fxvol_pct)         # 同上

final_scores = w_damage * damage_scores + w_fx * fx_scores

# -------------- 打印结果 --------------
print("=== Logistic 归一化后分数（0–100，越低越好）===")
print(f"{'Country':<10} {'Damage%':>10} {'D_Score':>10} {'FX%':>10} {'F_Score':>10} {'Final':>10}")
for c, d, ds, f, fs, fsum in zip(countries, damage_pct, damage_scores, fxvol_pct, fx_scores, final_scores):
    print(f"{c:<10} {d:10.4f} {ds:10.2f} {f:10.2f} {fs:10.2f} {fsum:10.2f}")

# -------------- 排序（从好到差） --------------
order = np.argsort(final_scores)  # 越低越好
print("\n=== 排名（越低越好） ===")
for rank, idx in enumerate(order, 1):
    print(f"{rank}. {countries[idx]}  Final={final_scores[idx]:.2f}  "
          f"(Damage={damage_scores[idx]:.2f}, FX={fx_scores[idx]:.2f})")

# -------------- 可选：想调灵敏度？手动设 T 例子 --------------
# 比如把两列的“温度”调大（更不敏感）或调小（更接近0/100）：
# damage_scores_T = logistic_scores(damage_pct, T=np.std(damage_pct, ddof=1)*1.5)
# fx_scores_T     = logistic_scores(fxvol_pct,     T=np.std(fxvol_pct, ddof=1)*1.5)
# final_T         = w_damage*damage_scores_T + w_fx*fx_scores_T
