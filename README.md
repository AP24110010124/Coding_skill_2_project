# 🌍 Smart Travel Itinerary Optimizer

> **CCC Algorithm Project** — Demonstrating Greedy & Dynamic Programming algorithms through real-world travel planning.

| Name | Registration No. |
|------|------------------|
| DHATRIKA | AP24110010085|
| RUDVI| AP24110010103|
| SASANK | AP24110010124|
| SRIRAM VISWA | AP24110010104|

---I 

## 📌 Problem Statement

Given a list of tourist destinations, each with a **visit cost** and an **enjoyment value**, find the best combination of places to visit within a **fixed budget** to maximize total enjoyment.

This is a classic **optimization problem** solved using two powerful algorithmic strategies:

| Algorithm | Strategy | Complexity |
|-----------|----------|------------|
| **Greedy** | Pick places with the best value/cost ratio first | O(n log n) |
| **Dynamic Programming** | 0/1 Knapsack — guaranteed optimal solution | O(n × budget) |

---

## 🧠 Algorithms Used

### 1. Greedy Algorithm
- **Idea:** Sort places by value-to-cost ratio. Pick the most "efficient" place first, then the next, until budget is exhausted.
- **Strength:** Very fast, intuitive
- **Weakness:** Does not always give the globally optimal answer

### 2. Dynamic Programming (0/1 Knapsack)
- **Idea:** Build a table `dp[i][w]` = max value using first `i` places within budget `w`
- **Strength:** Always finds the globally optimal subset
- **Weakness:** Higher time/space complexity — O(n × budget)

### Key Insight
> DP will always give a result **≥ Greedy**. The project lets you see exactly how much better DP performs.

---

## 🗂️ Project Structure

```
travel_optimizer/
│
├── algorithms.py       # Core: Greedy + DP implementations
├── data.py             # Dataset of 22 Indian tourist places
├── main.py             # CLI app — run this!
├── test_algorithms.py  # Unit tests (pytest)
└── README.md           # You're here
```

---
```

**Example interaction:**
```
Available Categories: Heritage | Nature | Beach | Spiritual | Culture | All
Enter category filter (or 'All'): All
Enter your total budget in ₹ (e.g. 5000): 3000
```

### Run Tests
```bash
python -m pytest test_algorithms.py -v
```

---

## 📊 Sample Output

```
  GREEDY ALGORITHM  (Best Ratio First)
  ────────────────────────────────────────────────────
  🕌  Varanasi Ghats, UP               ₹  300  [█████████ ] 91
  🏛️  Golden Temple, Amritsar          ₹  200  [█████████ ] 96
  🎭  Mysore Palace, Karnataka         ₹  400  [████████  ] 85
  💰  Total Cost  : ₹900  | ⭐ Value: 272

  DYNAMIC PROGRAMMING  (Optimal Knapsack)
  ────────────────────────────────────────────────────
  🕌  Varanasi Ghats, UP               ₹  300  [█████████ ] 91
  🏛️  Golden Temple, Amritsar          ₹  200  [█████████ ] 96
  🌿  Munnar Tea Gardens, Kerala       ₹  800  [█████████ ] 90
  🎭  Pondicherry French Quarter       ₹  300  [███████   ] 79
  💰  Total Cost  : ₹1600  | ⭐ Value: 356

  ✅  DP found a BETTER solution by +84 value points!
```

---

## 🔬 Algorithm Complexity Analysis

| | Greedy | DP (Knapsack) |
|--|--------|---------------|
| Time | O(n log n) | O(n × W) |
| Space | O(n) | O(n × W) |
| Optimal? | ❌ Not always | ✅ Always |
| Speed | Faster | Slower for large W |

Where `n` = number of places, `W` = budget

---

## 👥 Team

- Team Size: up to 5 members
- Submitted to: CCC GitHub

---

## 📄 License
MIT License
