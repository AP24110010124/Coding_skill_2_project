"""
test_algorithms.py
==================
Unit tests for Greedy and DP algorithms.
Run with: python -m pytest test_algorithms.py -v
"""

import unittest
from algorithms import Place, greedy_itinerary, dp_itinerary, compare_algorithms


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_places = [
            Place("A", cost=300, value=60, category="Heritage"),
            Place("B", cost=200, value=50, category="Nature"),
            Place("C", cost=500, value=90, category="Beach"),
            Place("D", cost=100, value=30, category="Culture"),
            Place("E", cost=400, value=70, category="Spiritual"),
        ]


# ── Greedy Tests ──────────────────────────────────────────

class TestGreedy:
    def test_basic(self, sample_places):
        selected, cost, value = greedy_itinerary(sample_places, 600)
        assert cost <= 600
        assert value > 0
        assert len(selected) > 0

    def test_zero_budget(self, sample_places):
        selected, cost, value = greedy_itinerary(sample_places, 0)
        assert selected == []
        assert cost == 0
        assert value == 0

    def test_large_budget(self, sample_places):
        selected, cost, value = greedy_itinerary(sample_places, 99999)
        assert len(selected) == len(sample_places)

    def test_cost_never_exceeds_budget(self, sample_places):
        for budget in [100, 300, 500, 800, 1500]:
            _, cost, _ = greedy_itinerary(sample_places, budget)
            assert cost <= budget

    def test_single_place(self):
        places = [Place("Only", cost=500, value=80, category="Heritage")]
        selected, cost, value = greedy_itinerary(places, 500)
        assert len(selected) == 1
        assert cost == 500


# ── DP Tests ──────────────────────────────────────────────

class TestDP:
    def test_basic(self, sample_places):
        selected, cost, value = dp_itinerary(sample_places, 600)
        assert cost <= 600
        assert value > 0

    def test_zero_budget(self, sample_places):
        selected, cost, value = dp_itinerary(sample_places, 0)
        assert selected == []
        assert value == 0

    def test_large_budget(self, sample_places):
        selected, cost, value = dp_itinerary(sample_places, 99999)
        assert len(selected) == len(sample_places)

    def test_dp_is_optimal(self, sample_places):
        """DP must return value >= Greedy for any budget."""
        for budget in [200, 500, 800, 1500]:
            _, _, g_val = greedy_itinerary(sample_places, budget)
            _, _, d_val = dp_itinerary(sample_places, budget)
            assert d_val >= g_val, f"DP not optimal at budget={budget}"

    def test_known_optimal(self):
        """Manually verifiable optimal result."""
        places = [
            Place("X", cost=100, value=60, category="A"),
            Place("Y", cost=200, value=100, category="B"),
            Place("Z", cost=300, value=120, category="C"),
        ]
        # Budget=300: best is Y+X=160, not Z=120
        _, _, value = dp_itinerary(places, 300)
        assert value == 160


# ── Comparison Tests ──────────────────────────────────────

class TestComparison:
    def test_compare_returns_both(self, sample_places):
        result = compare_algorithms(sample_places, 800)
        assert "greedy" in result
        assert "dp" in result
        assert "dp_advantage" in result

    def test_dp_advantage_correct(self, sample_places):
        result = compare_algorithms(sample_places, 800)
        expected = result["dp"]["total_value"] - result["greedy"]["total_value"]
        assert result["dp_advantage"] == expected
