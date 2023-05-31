def longestConsecutive(nums):
    nums = set(nums)
    longest = 0
    for i in nums:
        if i-1 not in nums:
            j = i
            while j in nums:
                j += 1
            longest = max(longest, j-i)
    return longest