"""Prototype pédagogique : engagement de chemin Merkle (hachage abstrait)."""

def parent(left, right):
    return f"{left}|{right}"

def root(leaf, path, index):
    value=leaf
    for sibling in path:
        value=parent(value,sibling) if index % 2 == 0 else parent(sibling,value)
        index //= 2
    return value

if __name__ == "__main__":
    assert root("L",["R"],0)=="L|R"
    assert root("R",["L"],1)=="L|R"
