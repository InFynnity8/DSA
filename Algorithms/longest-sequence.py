def longestSequence( nums) -> int:
        arr = sorted(nums)
        seq = []
        output = 0
        for num in arr:
            if num-1 not in arr:
                output = max(output, len(set(seq)))
                seq = []
                seq.append(num)
            else:    
                seq.append(num)
        return max(output, len(set(seq)))




def longestConsecutive(nums) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

nums = [0,-1,2,-2,3,-3,1,1]

print(longestConsecutive(nums))
m = "i Jwas 3dead?"
s = ''.join(a.lower() for a in m if a.isalnum())
