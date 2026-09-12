"""Prototype documentaire : protection contre replay et régression de nonce."""

def nonce_is_fresh(previous, candidate):
    return isinstance(previous, int) and isinstance(candidate, int) and candidate > previous

def accept_order(order, last_nonce, account):
    return (order.get("account") == account and nonce_is_fresh(last_nonce, order.get("nonce"))
            and bool(order.get("signature")))

if __name__ == "__main__":
    order={"account":"0xabc","nonce":8,"signature":"sig"}
    assert accept_order(order,7,"0xabc")
    assert not accept_order(order,8,"0xabc")
    assert not accept_order(order,7,"0xdef")
