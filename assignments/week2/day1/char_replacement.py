def characterReplacement(s, k):
    char_count = {}
    l=max_length = 0
    for r in range(len(s)):
        char_count[s[r]]=char_count.get(s[r],0)+1
        
        while (r-l+1)-max(char_count.values())>k:
            char_count[s[l]]-=1
            l+=1
        
        max_length=max(max_length,r-l+1)
    
    return max_length