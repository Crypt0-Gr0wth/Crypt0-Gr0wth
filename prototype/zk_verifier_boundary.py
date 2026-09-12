"""Prototype pédagogique : séparation des entrées publiques du vérificateur."""

PUBLIC_KEYS=("statement","proof","verification_key")

def verifier_input(payload):
    return isinstance(payload,dict) and all(payload.get(k) is not None for k in PUBLIC_KEYS)

def verify_boundary(payload, expected_statement):
    return verifier_input(payload) and payload["statement"]==expected_statement

if __name__ == "__main__":
    p={"statement":"S","proof":"P","verification_key":"VK"}
    assert verify_boundary(p,"S")
    assert not verify_boundary(p,"T")
