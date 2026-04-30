"""
algorithms.py
=============
Core algorithms used in the Travel Itinerary Optimizer:
  1. Greedy Algorithm  – selects top-rated places that fit within budget
  2. Dynamic Programming (0/1 Knapsack) – maximizes total value within budget
"""

from typing import List, Dict, Tuple


# ─────────────────────────────────────────────
#  Data structure
# ─────────────────────────────────────────────

class Place:
    def __init__(self, name: str, cost: int, value: int, category: str):
        self.name = name
        self.cost = cost        # entry / visit cost in ₹
        self.value = value      # enjoyment / rating score (0–100)
        self.category = category

    def __repr__(self):
        return f"Place({self.name}, cost=₹{self.cost}, value={self.value})"


# ─────────────────────────────────────────────
#  Greedy Algorithm
# ─────────────────────────────────────────────

def greedy_itinerary(places: List[Place], budget: int) -> Tuple[List[Place], int, int]:
    """
    Greedy strategy: sort places by value/cost ratio (best bang-for-buck first)
    and keep picking until budget runs out.

    Time Complexity : O(n log n)
    Space Complexity: O(n)

    Returns: (selected_places, total_cost, total_value)
    """
    # Sort descending by value-to-cost ratio
    sorted_places = sorted(places, key=lambda p: p.value / p.cost, reverse=True)

    selected = []
    total_cost = 0
    total_value = 0

    for place in sorted_places:
        if total_cost + place.cost <= budget:
            selected.append(place)
            total_cost += place.cost
            total_value += place.value

    return selected, total_cost, total_value


# ─────────────────────────────────────────────
#  Dynamic Programming – 0/1 Knapsack
# ─────────────────────────────────────────────

def dp_itinerary(places: List[Place], budget: int) -> Tuple[List[Place], int, int]:
    """
    DP (0/1 Knapsack): finds the globally OPTIMAL subset of places that
    maximises total value without exceeding budget.

    Time Complexity : O(n × budget)
    Space Complexity: O(n × budget)

    Returns: (selected_places, total_cost, total_value)
    """
    n = len(places)
    # dp[i][w] = max value using first i places with budget w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        place = places[i - 1]
        for w in range(budget + 1):
            # Don't take this place
            dp[i][w] = dp[i - 1][w]
            # Take this place if it fits
            if place.cost <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - place.cost] + place.value)

    # Backtrack to find which places were selected
    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(places[i - 1])
            w -= places[i - 1].cost

    selected.reverse()
    total_cost = sum(p.cost for p in selected)
    total_value = sum(p.value for p in selected)

    return selected, total_cost, total_value


# ─────────────────────────────────────────────
#  Comparison helper
# ─────────────────────────────────────────────

def compare_algorithms(places: List[Place], budget: int) -> Dict:
    """Run both algorithms and return a comparison dictionary."""
    g_places, g_cost, g_value = greedy_itinerary(places, budget)
    d_places, d_cost, d_value = dp_itinerary(places, budget)

    return {
        "greedy": {
            "places": g_places,
            "total_cost": g_cost,
            "total_value": g_value,
        },
        "dp": {
            "places": d_places,
            "total_cost": d_cost,
            "total_value": d_value,
        },
        "dp_advantage": d_value - g_value,
    }
