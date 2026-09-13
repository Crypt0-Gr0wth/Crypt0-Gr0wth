"""Deterministic snapshot checks for Base fee parameters."""
from dataclasses import dataclass

@dataclass(frozen=True)
class FeeSnapshot:
    block: int
    base_fee: int
    blob_base_fee: int | None
    observed_at: int

def validate(previous: FeeSnapshot | None, current: FeeSnapshot) -> list[str]:
    errors = []
    if current.block < 0 or current.base_fee < 0:
        errors.append("negative block or fee")
    if current.blob_base_fee is not None and current.blob_base_fee < 0:
        errors.append("negative blob fee")
    if previous and current.block <= previous.block:
        errors.append("non-monotonic block")
    if previous and current.observed_at < previous.observed_at:
        errors.append("observation time moved backwards")
    return errors

if __name__ == "__main__":
    print(validate(None, FeeSnapshot(1, 1, None, 10)))
