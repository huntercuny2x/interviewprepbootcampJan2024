def maxAreaBrute(height):
    max_area = 0
    for l in range(height):
        for r in range(l+1,height):
            area = (r-l)*min(height[r],height[l])
            max_area = max(max_area,area)
    
    return max_area


def maxArea(height):
    l,r, max_area=0,len(height)-1,0
    
    while l<r:
        area=(r-l)*min(height[l],height[r])
        max_area=max(max_area, area)

        if height[l] > height[r]:
            r-=1
        
        else:
            l+=1
    
    return max_area
