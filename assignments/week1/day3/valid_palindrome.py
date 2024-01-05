def isPalindromeMemory(s):
    s1=''
    for c in s:
        if c.isalnum():
            s1+=c.lower()
    return  s1==s1[::-1]

def isPalindromeBetterMemory(s):
    l, r = 0, len(s)-1
    while l<r:
        if not s[l].isalnum():
            l+=1
            continue
        
        if not s[r].isalnum():
            r-=1
            continue

        if s[l].lower() != s[r].lower():
            return False
        l , r = l+1, r-1
    
    return True