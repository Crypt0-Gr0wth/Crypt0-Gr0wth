"""Prototype pédagogique : liaison déterministe d'un transcript."""

def challenge(statement, commitment, nonce):
    return hash((statement, commitment, nonce))

def bound(statement, commitment, nonce, response, claimed):
    return challenge(statement,commitment,nonce)==claimed and response is not None

if __name__ == "__main__":
    c=challenge("x=7","C","n1")
    assert bound("x=7","C","n1","r",c)
    assert not bound("x=8","C","n1","r",c)
