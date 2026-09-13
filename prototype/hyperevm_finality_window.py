"""Documentary classifier for block observations and finality windows."""
from enum import Enum

class Confidence(str, Enum):
    UNKNOWN = "unknown"
    OBSERVED = "observed"
    REORG_RISK = "reorg-risk"
    CONFIRMED = "confirmed"
    FINAL = "final"

def classify(depth: int, reorg_window: int, finality_depth: int) -> Confidence:
    if min(depth, reorg_window, finality_depth) < 0 or reorg_window > finality_depth:
        return Confidence.UNKNOWN
    if depth == 0:
        return Confidence.OBSERVED
    if depth <= reorg_window:
        return Confidence.REORG_RISK
    if depth < finality_depth:
        return Confidence.CONFIRMED
    return Confidence.FINAL

if __name__ == "__main__":
    print(classify(12, 3, 10).value)
