"""Prototype documentaire : garde-fou de chaîne et de bloc HyperEVM."""

def block_is_expected(block, chain_id, parent_hash, minimum_timestamp):
    required=("chain_id","number","parent_hash","timestamp","hash")
    if not isinstance(block,dict) or any(block.get(k) is None for k in required):
        return False
    return (block["chain_id"]==chain_id and block["parent_hash"]==parent_hash
            and block["timestamp"] >= minimum_timestamp and block["number"] >= 0
            and block["hash"] != block["parent_hash"])

if __name__ == "__main__":
    b={"chain_id":999,"number":2,"parent_hash":"h1","timestamp":100,"hash":"h2"}
    assert block_is_expected(b,999,"h1",90)
    assert not block_is_expected({**b,"chain_id":1},999,"h1",90)
