"""
main.py
=======
Smart Travel Itinerary Optimizer
---------------------------------
Uses Greedy and Dynamic Programming (0/1 Knapsack) algorithms
to plan the best trip within a given budget.

Run:
    python main.py
"""

from algorithms import compare_algorithms, greedy_itinerary, dp_itinerary
from data import SAMPLE_PLACES

BANNER = """
╔══════════════════════════════════════════════════════════╗
║       🌍  Smart Travel Itinerary Optimizer  ✈️           ║
║    Algorithms: Greedy + Dynamic Programming (Knapsack)   ║
╚══════════════════════════════════════════════════════════╝
"""

CATEGORY_ICONS = {
    "Heritage":  "🏛️",
    "Nature":    "🌿",
    "Beach":     "🏖️",
    "Spiritual": "🕌",
    "Culture":   "🎭",
}


def print_itinerary(places, total_cost, total_value, budget, label):
    print(f"\n  {'─'*52}")
    print(f"  📋  {label}")
    print(f"  {'─'*52}")
    if not places:
        print("  ⚠️  No places fit within budget.")
        return
    for p in places:
        icon = CATEGORY_ICONS.get(p.category, "📍")
        bar = "█" * (p.value // 10)
        print(f"  {icon}  {p.name:<35} ₹{p.cost:>5}  [{bar:<10}] {p.value}")
    print(f"  {'─'*52}")
    print(f"  💰  Total Cost  : ₹{total_cost}  (Budget: ₹{budget}, Remaining: ₹{budget - total_cost})")
    print(f"  ⭐  Total Value : {total_value} / {len(places) * 100}")
    print(f"  🗺️  Places Count: {len(places)}")


def filter_by_category(places, category):
    if category.lower() == "all":
        return places
    return [p for p in places if p.category.lower() == category.lower()]


def main():
    print(BANNER)

    # ── Input ──────────────────────────────────────────────
    print("  Available Categories: Heritage | Nature | Beach | Spiritual | Culture | All")
    category = input("  Enter category filter (or 'All'): ").strip() or "All"
    budget_input = input("  Enter your total budget in ₹ (e.g. 5000): ").strip()

    try:
        budget = int(budget_input)
        if budget <= 0:
            raise ValueError
    except ValueError:
        print("  ❌ Invalid budget. Please enter a positive integer.")
        return

    places = filter_by_category(SAMPLE_PLACES, category)
    if not places:
        print(f"  ❌ No places found for category: {category}")
        return

    print(f"\n  Found {len(places)} places in category '{category}' to evaluate.\n")

    # ── Run Algorithms ─────────────────────────────────────
    result = compare_algorithms(places, budget)

    g = result["greedy"]
    d = result["dp"]

    print_itinerary(g["places"], g["total_cost"], g["total_value"], budget,
                    "GREEDY ALGORITHM  (Best Ratio First)")

    print_itinerary(d["places"], d["total_cost"], d["total_value"], budget,
                    "DYNAMIC PROGRAMMING  (Optimal Knapsack)")

    # ── Comparison Summary ─────────────────────────────────
    print(f"\n  {'═'*52}")
    print("  📊  ALGORITHM COMPARISON SUMMARY")
    print(f"  {'═'*52}")
    print(f"  {'Metric':<25} {'Greedy':>10} {'DP':>10}")
    print(f"  {'─'*47}")
    print(f"  {'Places Selected':<25} {len(g['places']):>10} {len(d['places']):>10}")
    print(f"  {'Total Cost (₹)':<25} {g['total_cost']:>10} {d['total_cost']:>10}")
    print(f"  {'Total Value Score':<25} {g['total_value']:>10} {d['total_value']:>10}")
    adv = result["dp_advantage"]
    if adv > 0:
        print(f"\n  ✅  DP found a BETTER solution by +{adv} value points!")
    elif adv == 0:
        print(f"\n  🤝  Both algorithms found equally optimal solutions!")
    else:
        print(f"\n  ⚡  Greedy was competitive this time (rare edge case).")

    print(f"\n  {'═'*52}")
    print("  💡  Recommendation: Use DP result for the best trip!\n")


if __name__ == "__main__":
    main()
