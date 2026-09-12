"""Prototype documentaire : transitions sûres du cycle d'un ordre."""

TRANSITIONS={"new":{"submitted","cancelled"},"submitted":{"partially_filled","filled","cancelled"},"partially_filled":{"filled","cancelled"},"filled":set(),"cancelled":set()}

def valid_transition(previous, current):
    return current in TRANSITIONS.get(previous,set())

def apply_event(state, event):
    if event.get("order_id") != state.get("order_id"):
        return None
    if not valid_transition(state.get("status"),event.get("status")):
        return None
    return {"order_id":state["order_id"],"status":event["status"]}

if __name__ == "__main__":
    s={"order_id":"o1","status":"new"}
    assert apply_event(s,{"order_id":"o1","status":"submitted"})["status"]=="submitted"
    assert apply_event(s,{"order_id":"o1","status":"filled"}) is None
