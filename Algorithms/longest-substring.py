def lengthOfLongestSubstring(s: str) -> int:
    length = 0
    l = 0
    for r in range(len(s)):
        while s[r] in s[l:r]:
            l += 1
        length = max(length, r - l + 1)
    return length


p = 'h'
s = "hheadingsttseeeeeeee"
print(lengthOfLongestSubstring(p))
