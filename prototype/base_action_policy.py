"""Prototype documentaire : politique d'autorisation d'actions pour un agent Base."""

def is_allowed(action, allowlist):
    return action in set(allowlist)

def requires_approval(action, value, threshold):
    return action == "transfer" or value >= threshold

def decision(action, value, allowlist, threshold, approved=False):
    if not is_allowed(action, allowlist): return "deny"
    if requires_approval(action, value, threshold) and not approved: return "approval_required"
    return "allow"

if __name__ == "__main__":
    assert decision("read_balance", 0, ["read_balance"], 100) == "allow"
    assert decision("transfer", 1, ["transfer"], 100) == "approval_required"
    assert decision("admin_call", 0, ["read_balance"], 100) == "deny"
