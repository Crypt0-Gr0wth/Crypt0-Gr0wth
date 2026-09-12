"""Prototype pédagogique : précondition d'une preuve de plage."""

def range_statement(value, lower, upper):
    if not all(isinstance(x,int) for x in (value,lower,upper)) or lower>upper:
        raise ValueError("invalid range")
    return {"commitment":hash((value,lower,upper)),"lower":lower,"upper":upper}

def witness_satisfies(value, statement):
    return statement["lower"] <= value <= statement["upper"]

if __name__ == "__main__":
    s=range_statement(7,1,10)
    assert witness_satisfies(7,s)
    assert not witness_satisfies(12,s)
