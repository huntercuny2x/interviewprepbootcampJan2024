def isAnagramSort(s, t):
    return sorted(s)==sorted(t)


def isAnagramMap(s, t):
    if len(s) != len(t):
        return False

    map_s, map_t = {},{}
    for i in range(len(s)):
        if s[i] in map_s:
            map_s[s[i]]=map_s[s[i]]+1
        else:
            map_s[s[i]]=1
        
        if t[i] in map_t:
            map_t[t[i]]=map_t[t[i]]+1
        else:
            map_t[t[i]]=1

    return map_s==map_t


def isAnagramMapShort(s, t):
    if len(s) != len(t):
        return False

    map_s, map_t = {},{}
    for i in range(len(s)):
        map_s[s[i]]=map_s.get(s[i],0)+1
        map_t[t[i]]=map_s.get(t[i],0)+1

    return map_s==map_t