"""Prototype documentaire : provenance minimale d'une décision Base."""

def valid_provenance(event):
    required = ("source", "chain_id", "block_number", "observed_at")
    return isinstance(event, dict) and all(event.get(k) is not None for k in required)

def same_chain(event, expected_chain):
    return valid_provenance(event) and event["chain_id"] == expected_chain

def accept(event, expected_chain, max_age, now):
    return same_chain(event, expected_chain) and 0 <= now-event["observed_at"] <= max_age

if __name__ == "__main__":
    e={"source":"l2-node","chain_id":8453,"block_number":100,"observed_at":1000}
    assert accept(e,8453,30,1010)
    assert not accept(e,10,30,1010)
    assert not accept(e,8453,30,1040)
