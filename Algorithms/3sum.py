def threeSum(nums):
    res = []
    s = sorted(nums)

    for i in range(len(s)-2):
        j, k = i+1, len(s) - 1
        while j < k:
            if (s[j] + s[k]) == -s[i] and [s[i], s[j], s[k]] not in res:
                res.append([s[i], s[j], s[k]])
                j += 1
                k -= 1
            elif (s[j] + s[k]) < -s[i]:
                j += 1
            else:
                k -= 1
    return res


nums=[-1,0,1,0]   

print(threeSum(nums))
