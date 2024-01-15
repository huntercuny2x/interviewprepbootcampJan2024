import heapq

def lastStoneWeight(stones):
    stones_q=[]
    for i in range(len(stones)):
        heapq.heappush(stones_q, -1*stones[i])

    while len(stones_q)>=2:
        y=heapq.heappop(stones_q)
        x=heapq.heappop(stones_q)
        if x!=y:
            heapq.heappush(stones_q, y-x)

    return abs(heapq.heappop(stones_q)) if stones_q else 0