def groupAnagramsSort(strs):
    map1 = {}
    for s in strs:
        t=''.join(sorted(s))
        if t in map1:
            map1[t].append(s)
        else:
            map1[t]=[s]
    return map1.values()


def groupAnagramTupleDict(strs):
    map1 = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        if tuple(count) in map1:
            map1[tuple(count)].append(s)
        else:
            map1[tuple(count)]=[s]

    return map1.values()

