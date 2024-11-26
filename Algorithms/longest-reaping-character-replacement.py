def characterReplacement(s: str, k: int) -> int:
    count = {}
    length = 0
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf> k:
            count[s[l]] -= 1
            l += 1
        length = max(length, r - l + 1)

    return length

stack =[-1,3,4,5]
s = "XYYXrffddasfcdddd"
k = 2
print(characterReplacement(s, k))
print(stack[-1::-1].index(3))
