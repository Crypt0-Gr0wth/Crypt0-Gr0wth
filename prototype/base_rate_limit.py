"""Prototype documentaire : fenêtre de débit pour un agent Base."""

def within_budget(events, start, now, limit, window):
    if not all(isinstance(x,int) for x in (start,now,limit,window)) or now < start:
        return False
    recent=[t for t in events if start <= t <= now]
    return now-start <= window and len(recent) <= limit

if __name__ == "__main__":
    assert within_budget([1,3,5],0,5,3,10)
    assert not within_budget([1,3,5,6],0,6,3,10)
    assert not within_budget([1],0,11,3,10)
