# Tesla Case Study: Manufacturing Cost Analysis

## Overview

This project analyzes manufacturing costs for lamp production across three potential locations: **United States**, **Mexico**, and **China**. The analysis considers raw material costs, labor, tariffs, and most importantly, the impact of **production yield rates** on the effective per-unit cost during a 6-month production ramp-up period.

## Cost Breakdown

The following cost components (in USD per unit) are analyzed for each location:

| Component | US | Mexico | China |
|-----------|------|--------|-------|
| Raw material | $40 | $35 | $30 |
| Labor | $12 | $8 | $4 |
| Indirect costs | $10 | $8 | $4 |
| Packaging/transport/inventory | $9 | $7 | $12 |
| Electricity | $4 | $3 | $4 |
| Depreciation | $5 | $1 | $5 |
| Tariff costs | $0 | $15.50 | $15 |
| **Total (baseline)** | **$80** | **$77.50** | **$74** |

## Yield Analysis

The key insight is that production yield significantly impacts the effective cost per good unit. During the initial 6-month ramp-up period, yield rates improve from initial levels to (near) 100%:

- **US**: 80% → 100%
- **Mexico**: 90% → 100%
- **China**: 95% → 99%

The effective price per good lamp is calculated as:
```
Price per good unit = Baseline cost / Yield rate
```

## Scripts

### 1. `cost_exp.py` - Smooth Yield Ramp Model

This script models a **continuous, smooth improvement** in yield rates over the 6-month period.

**Features:**
- Uses an ease-out quadratic function for US and Mexico
- Uses an exponential approach function for China (asymptotically approaching 99%)
- Plots per-lamp cost curves showing gradual cost reduction
- Provides a realistic view of production ramp-up

**Usage:**
```bash
python cost_exp.py
```

**Output:**
- Interactive matplotlib plot showing cost evolution over 6 months
- Console output with baseline costs

### 2. `cost_pw.py` - Piecewise Constant Model

This script models a **sudden yield improvement** at the 6-month mark.

**Features:**
- Yields stay constant at initial rates for the first 6 months
- Sudden jump to 100% (or target) yield at month 6
- Uses step plots to visualize discrete cost changes
- Useful for conservative cost analysis or milestone-based planning

**Usage:**
```bash
python cost_pw.py
```

**Output:**
- Interactive matplotlib plot with step functions
- Vertical dashed line at the 6-month transition point

## Requirements

Install the required Python packages:

```bash
pip install numpy pandas matplotlib
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

## Key Findings

1. **Initial Cost Advantage**: Despite having the lowest baseline cost ($74), China's effective cost advantage diminishes when accounting for yield inefficiencies during ramp-up.

2. **US Cost Impact**: The US starts at $100/lamp (80% yield) but drops to $80/lamp at full yield, showing the most dramatic improvement.

3. **Mexico's Position**: Mexico maintains a middle ground with moderate baseline costs ($77.50) and good initial yield (90%).

4. **Long-term vs. Short-term**: The analysis shows that location decisions should consider not just steady-state costs, but also ramp-up dynamics and time-to-profitability.

## Customization

You can adjust the following parameters in either script:

- **Initial yield rates**: Modify `y0_US`, `y0_MX`, `y0_CN`
- **Baseline costs**: Edit the data dictionary in `cost_exp.py`
- **Time horizon**: Adjust the `months` array
- **Target yields**: Change the final yield values

## Analysis Questions

This model helps answer questions like:
- How long does it take for each location to reach target cost levels?
- What is the cumulative cost difference during ramp-up?
- Which location offers the best total cost of ownership over different time periods?
- How sensitive is the decision to initial yield assumptions?

## License

This project is for educational and case study purposes.

---

**Last Updated:** October 2025

