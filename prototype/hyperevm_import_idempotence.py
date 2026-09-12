"""Prototype documentaire : import idempotent d'un bloc HyperEVM."""

def import_block(state, block):
    number, digest = block["number"], block["digest"]
    if number <= state["height"]:
        return state if state["digests"].get(number) == digest else None
    if number != state["height"] + 1:
        return None
    updated={"height":number,"digests":dict(state["digests"])}
    updated["digests"][number]=digest
    return updated

if __name__ == "__main__":
    s={"height":1,"digests":{1:"a"}}
    assert import_block(s,{"number":2,"digest":"b"})["height"]==2
    assert import_block(s,{"number":1,"digest":"a"})==s
    assert import_block(s,{"number":3,"digest":"c"}) is None
