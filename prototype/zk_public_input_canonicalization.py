"""Stable encoding for documentary ZK public-input commitments."""
from hashlib import sha256

def encode_inputs(values: list[int]) -> bytes:
    if any(value < 0 for value in values):
        raise ValueError("public inputs must be non-negative")
    return b"".join(value.to_bytes(32, "big") for value in values)

def commitment(domain: str, circuit: str, values: list[int]) -> str:
    if not domain or not circuit:
        raise ValueError("domain and circuit are required")
    prefix = f"{domain}:{circuit}:{len(values)}:".encode()
    return sha256(prefix + encode_inputs(values)).hexdigest()

if __name__ == "__main__":
    print(commitment("payments-v1", "circuit-1", [3, 5]))
