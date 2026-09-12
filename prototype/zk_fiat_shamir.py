"""Prototype pédagogique : challenge Fiat-Shamir lié aux engagements."""

def derive_challenge(statement, commitment, domain="zk-proof-v1"):
    return hash((domain, statement, commitment))

def verify_challenge(statement, commitment, challenge, domain="zk-proof-v1"):
    return derive_challenge(statement,commitment,domain)==challenge

if __name__ == "__main__":
    c=derive_challenge("statement","commitment")
    assert verify_challenge("statement","commitment",c)
    assert not verify_challenge("other","commitment",c)
