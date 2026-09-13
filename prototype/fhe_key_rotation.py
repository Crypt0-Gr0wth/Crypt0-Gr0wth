"""Policy model for versioned FHE keys during rotation."""
from dataclasses import dataclass

@dataclass(frozen=True)
class KeyVersion:
    version: int
    valid_from: int
    valid_until: int | None
    revoked: bool = False

def usable(key: KeyVersion, now: int) -> bool:
    if key.revoked or now < key.valid_from:
        return False
    return key.valid_until is None or now < key.valid_until

def choose(keys: list[KeyVersion], now: int) -> KeyVersion | None:
    candidates = [key for key in keys if usable(key, now)]
    return max(candidates, key=lambda key: key.version, default=None)

if __name__ == "__main__":
    print(choose([KeyVersion(1, 0, 100), KeyVersion(2, 90, None)], 95))
