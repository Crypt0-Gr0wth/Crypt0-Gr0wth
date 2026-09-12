"""Checks transversaux pour les prototypes documentaires."""
import unittest

def fresh_enough(observed, reference, max_age):
    return (isinstance(observed, int) and isinstance(reference, int) and isinstance(max_age, int)
            and 0 <= observed - reference <= max_age)

def monotonic(previous, current):
    return isinstance(previous, int) and isinstance(current, int) and current >= previous

def bounded(value, low, high):
    return (all(isinstance(x, int) for x in (value, low, high))
            and low <= high and low <= value <= high)

class InvariantTests(unittest.TestCase):
    def test_fresh_observation(self): self.assertTrue(fresh_enough(105, 100, 10))
    def test_stale_observation(self): self.assertFalse(fresh_enough(120, 100, 10))
    def test_monotonic_cursor(self): self.assertTrue(monotonic(8, 9))
    def test_cursor_regression(self): self.assertFalse(monotonic(9, 8))
    def test_range_claim(self): self.assertTrue(bounded(7, 1, 10))
    def test_invalid_range(self): self.assertFalse(bounded(12, 1, 10))

if __name__ == "__main__": unittest.main()
