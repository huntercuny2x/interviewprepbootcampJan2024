import heapq

def kClosest(points, k):
    dists_heap=[]
    for i, point in enumerate(points):
        heapq.heappush(dists_heap,[sqrt(point[0]**2 + point[1]**2),i])

    k_points=[]
    for i in range(k):
        elem=heapq.heappop(dists_heap)
        k_points.append(points[elem[1]])
    
    return k_points