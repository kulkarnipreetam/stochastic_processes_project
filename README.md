# 📈 Apple Stock Price Analysis using Markov Chains

## 📘 Introduction & Background

This project explores the use of **Markov Chains** to model and simulate the daily return of **Apple's stock** based on historical data. In the ever-changing financial market, stock price movements are influenced by company performance, economic indicators, and investor behavior. By leveraging a stochastic modeling approach, this analysis aims to uncover transition dynamics in Apple's returns, offering insights into trend behavior and helping investors make data-informed decisions.

---

## 🎯 Problem Statement

The goal of this project is to:

- Analyze Apple's historical stock prices.
- Use Markov Chains to define states based on daily returns.
- Calculate transition probabilities and long-run behavior.
- Simulate possible future stock prices to guide investment decisions.

---

## 🔍 Methodology

1. **Data Collection**: Apple stock closing prices were retrieved from Google Finance for a period of ~2035 trading days.
2. **Daily Returns**: Daily returns were calculated and visualized, revealing a fat-tailed, non-normal distribution.
3. **State Definition**: Returns were divided into 4 states based on percentiles:

| State | Description   | Percentile Range | Return Range (%)        |
|:-------:|:---------------|:------------------:|:--------------------------:|
| 1     | Bear          | 0–25%            | -12.87 to -0.76         |
| 2     | Stagnant      | 26–50%           | -0.77 to 0.08           |
| 3     | Low Return    | 51–75%           | 0.09 to 1.03            |
| 4     | Bull          | 76–100%          | 1.04 to 11.97           |

4. **Transition Matrix (P-Matrix)**:
   - Represents one-step transition probabilities between states.
   - Ensures ergodicity and irreducibility.

| From \ To |   State 1   |   State 2   |   State 3   |   State 4   |
|:-----------|:-------------:|:-------------:|:-------------:|:-------------:|
| **State 1** |   0.297     |   0.169     |   0.220     |   0.313     |
| **State 2** |   0.234     |   0.263     |   0.285     |   0.218     |
| **State 3** |   0.207     |   0.308     |   0.266     |   0.219     |
| **State 4** |   0.259     |   0.261     |   0.228     |   0.251     |

5. **Steady-State Probabilities**:
   - Converge quickly to: π = (0.2493, 0.2504, 0.25, 0.2503)
   - Mean recurrence times: all ~4 transitions.

6. **Simulation**:
   - Starting stock price: **$166**, initial state: **Bear (1)**
   - Simulated stock prices over 50 days using Monte Carlo simulation.

---

## 📊 Results & Visualizations

- **Single 50-Day Simulation**: Showed both profit and loss opportunities.
- **1000 Simulations**:
  - Mean final price ≈ **$161.94**
  - 5th percentile ≈ **$79.9**, 95th percentile ≈ **$275.7**
  - Possible closing prices ranged from **$37.25 to $462.95**

---

## 🧾 Conclusion

- Markov Chains effectively modeled and simulated stock return dynamics.
- The system reached a steady-state after only a few transitions.
- While simulations give an insight into possible future behaviors, external factors like news, company policies, product launches, and geopolitical events must also be considered before making investment decisions.
- This methodology can be adapted for shorter durations or other stocks to assist in identifying profitable investment windows.

---

## 🛠️ Technologies Used

- Python (NumPy, Pandas, Matplotlib)
- Google Finance (for historical data)
- Markov Chain & Monte Carlo Simulation principles

---

## 📚 References

- Apple Inc. stock data: [Google Finance](https://www.google.com/finance/)
- Markov Chain Theory: Applied Stochastic Processes (IE 5309)

---

## Important Notice

The code in this repository is proprietary and protected by copyright law. Unauthorized copying, distribution, or use of this code is strictly prohibited. By accessing this repository, you agree to the following terms:

- **Do Not Copy:** You are not permitted to copy any part of this code for any purpose.
- **Do Not Distribute:** You are not permitted to distribute this code, in whole or in part, to any third party.
- **Do Not Use:** You are not permitted to use this code, in whole or in part, for any purpose without explicit permission from the owner.

If you have any questions or require permission, please contact the repository owner.

Thank you for your cooperation.
