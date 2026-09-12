"""Prototype documentaire : validation de fraîcheur et de séquence d'oracle."""

def oracle_is_usable(update, now, max_age, previous_round=0):
    required=("round_id","answer","updated_at")
    if not isinstance(update,dict) or any(update.get(k) is None for k in required):
        return False
    return (update["round_id"] > previous_round and 0 <= now-update["updated_at"] <= max_age
            and isinstance(update["answer"],(int,float)) and update["answer"] >= 0)

if __name__ == "__main__":
    u={"round_id":8,"answer":101.2,"updated_at":100}
    assert oracle_is_usable(u,110,30,7)
    assert not oracle_is_usable(u,140,30,7)
    assert not oracle_is_usable(u,110,30,8)
