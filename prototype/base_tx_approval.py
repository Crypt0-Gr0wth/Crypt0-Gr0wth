"""Prototype documentaire : approbation explicite d'une transaction Base."""

ALLOWED_METHODS={"transfer", "swap"}

def transaction_digest(tx):
    fields=(tx.get("chain_id"),tx.get("to"),tx.get("value"),tx.get("method"),tx.get("nonce"))
    return hash(fields)

def approval_required(tx, expected_chain, max_value):
    return (tx.get("chain_id")==expected_chain and tx.get("method") in ALLOWED_METHODS
            and isinstance(tx.get("value"),int) and 0 <= tx["value"] <= max_value)

def approve(tx, expected_chain, max_value, reviewed_digest):
    return approval_required(tx,expected_chain,max_value) and transaction_digest(tx)==reviewed_digest

if __name__ == "__main__":
    tx={"chain_id":8453,"to":"0xapp","value":10,"method":"transfer","nonce":4}
    d=transaction_digest(tx)
    assert approve(tx,8453,100,d)
    assert not approve({**tx,"chain_id":1},8453,100,d)
    assert not approve({**tx,"value":101},8453,100,d)
