"""Canonical action fingerprints for retry and signing reconciliation."""
from hashlib import sha256
from typing import Mapping

REQUIRED = ("action", "nonce", "signature_scope")

def canonical_payload(action: Mapping[str, object]) -> bytes:
    missing = [key for key in REQUIRED if key not in action]
    if missing:
        raise ValueError("missing fields: " + ",".join(missing))
    fields = [f"{key}={action[key]}" for key in sorted(action)]
    return "|".join(fields).encode()

def action_hash(action: Mapping[str, object]) -> str:
    return sha256(canonical_payload(action)).hexdigest()

if __name__ == "__main__":
    print(action_hash({"action": "order", "nonce": 7, "signature_scope": "main"}))
