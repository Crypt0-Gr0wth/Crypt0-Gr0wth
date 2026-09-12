"""Prototype documentaire : confirmation minimale après réorganisation L2."""


def confirmation_depth(head, observed, required):
    if not all(isinstance(x,int) for x in (head,observed,required)):
        return False
    return head >= observed and required >= 0 and head-observed >= required

def canonical_observation(block):
    return isinstance(block,dict) and bool(block.get("hash")) and block.get("parent_hash") is not None

if __name__ == "__main__":
    assert confirmation_depth(120,100,20)
    assert not confirmation_depth(119,100,20)
    assert canonical_observation({"hash":"h2","parent_hash":"h1"})
