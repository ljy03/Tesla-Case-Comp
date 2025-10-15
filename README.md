# Tesla Case Study: Multi-Criteria Sourcing Decision Analysis

## Overview

This project provides a comprehensive sourcing decision analysis for Tesla's automotive component manufacturing across three potential locations: **United States**, **Mexico**, and **China**. The analysis employs multiple methodologies including:

- **Multi-criteria weighted scoring** (Cost, Risk, Logistics)
- **Transport cost modeling** with uncertainty
- **AHP (Analytic Hierarchy Process)** for strategic decision-making
- **Monte Carlo simulation** for stochastic cost forecasting
- **Yield ramp analysis** during production startup

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

### 1. `final_model.py` - Multi-Criteria Decision Model ⭐ **PRIMARY ANALYSIS**

This is the **main decision model** that combines Cost, Risk, and Logistics factors with custom weights to rank sourcing locations.

**Features:**
- **Weighted scoring**: Cost 60%, Risk 25%, Logistics 15%
- Direct use of your final input values (no normalization)
- Generates two publication-ready graphs:
  - `tesla_sourcing_scores.png` - Full scale view
  - `tesla_sourcing_scores_zoomed.png` - Zoomed view highlighting differences
- Exports results to `tesla_ahp_scores.csv`
- Countries sorted from best to worst composite score

**Usage:**
```bash
python final_model.py
```

**Output:**
- Console table with all metrics and composite scores
- Two high-resolution PNG graphs (300 DPI)
- CSV file for further analysis

**Results:**
- **USA**: Best overall score (32-34 range) - Recommended choice
- **Mexico**: Middle performer (38-40 range)
- **China**: Highest scores (40-42 range)

### 2. `tesla.ipynb` - Comprehensive Jupyter Analysis

Interactive notebook containing three major analyses:

**Cell 0: Transport Cost Analysis**
- Deterministic calculation of logistics costs
- Models ocean freight (China), trucking (Mexico/US)
- Includes holding costs, air freight contingencies, and crisis scenarios

**Cell 1: AHP (Analytic Hierarchy Process)**
- Multi-criteria decision framework
- Evaluates across Cost, Risk, Logistics, and Supply Chain Readiness
- Uses pairwise comparison matrices
- Calculates consistency ratios to validate judgments

**Cell 2: Monte Carlo Simulation**
- 20,000 scenarios modeling uncertainty in all cost factors
- Generates probability distributions for landed costs
- Outputs p10, p50, p90 percentiles for risk assessment
- Calculates probability each region is cheapest

**Usage:**
```bash
jupyter notebook tesla.ipynb
```

### 3. `cost_exp.py` - Smooth Yield Ramp Model

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

### 4. `cost_pw.py` - Piecewise Constant Model

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

## Output Files

After running the analyses, you'll find the following generated files:

- **`tesla_sourcing_scores.png`** - Main decision model visualization (full scale)
- **`tesla_sourcing_scores_zoomed.png`** - Zoomed view emphasizing score differences
- **`tesla_ahp_scores.csv`** - Detailed scoring data for all countries
- **Jupyter notebook outputs** - Interactive plots and statistical summaries

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

### Multi-Criteria Decision Analysis (Primary Results)

1. **USA is the Recommended Choice**: With composite scores of 32-34, the USA emerges as the best option when balancing Cost (60%), Risk (25%), and Logistics (15%) factors.

2. **Risk and Logistics Drive USA Advantage**: While USA has higher raw costs, it excels in:
   - **Lowest Risk Score**: 32.23 (vs. Mexico 62.24, China 54.23)
   - **Strong Logistics**: 21.76 (vs. Mexico 19.12, China 59.12)
   - Minimal geopolitical and supply chain disruption risk

3. **Mexico as Middle Ground**: Scores 38-40 range. Excellent logistics (best at 19.12) but higher risk profile limits overall competitiveness.

4. **China's Cost Advantage Offset**: Despite lowest raw costs (29.50-31.97), China scores highest overall (40-42) due to:
   - Significantly poor logistics (59.12)
   - Elevated geopolitical risk (54.23)
   - Long lead times and supply chain complexity

5. **Minimal Change Over Time**: Scores remain relatively stable between 0-6 months and 6+ months periods, indicating decisions are driven more by structural factors than ramp-up dynamics.

### Yield and Cost Analysis

6. **Initial Cost Advantage**: Despite having the lowest baseline cost ($74), China's effective cost advantage diminishes when accounting for yield inefficiencies during ramp-up.

7. **US Cost Impact**: The US starts at $100/lamp (80% yield) but drops to $80/lamp at full yield, showing the most dramatic improvement.

8. **Long-term vs. Short-term**: Location decisions should consider not just steady-state costs, but also ramp-up dynamics, risk exposure, and total cost of ownership.

## Customization

### In `final_model.py`:
- **Weights**: Modify `W_COST`, `W_RISK`, `W_LOG` to change criteria importance
- **Input values**: Update `logistics`, `cost_0_6`, `cost_6p`, `risk` arrays
- **Graph colors**: Edit `colors_map` dictionary
- **Output filenames**: Change `plt.savefig()` parameters

### In yield analysis scripts:
- **Initial yield rates**: Modify `y0_US`, `y0_MX`, `y0_CN`
- **Baseline costs**: Edit the data dictionary
- **Time horizon**: Adjust the `months` array
- **Target yields**: Change the final yield values

## Analysis Questions Answered

This comprehensive framework addresses:

### Strategic Questions:
- Which sourcing location optimizes cost, risk, and logistics simultaneously?
- How should we weight different decision criteria?
- What is the probability distribution of landed costs under uncertainty?
- How do geopolitical risks impact the sourcing decision?

### Operational Questions:
- What are the expected transport costs for each route?
- How long does it take for each location to reach target cost levels?
- What is the cumulative cost difference during ramp-up?
- How sensitive is the decision to yield assumptions and crisis scenarios?

### Risk Questions:
- What is the 90th percentile cost outcome (worst-case planning)?
- Which location has the highest supply chain resilience?
- How do tariffs and trade policies affect the decision?

## License

This project is for educational and case study purposes.

---

**Last Updated:** October 2025

