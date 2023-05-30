def twoSum(nums, target):
    test_list = {}
    for i in range(len(nums)):
        if target - nums[i] in test_list:
            return [test_list[target - nums[i]], i]
        else:
            test_list.update({nums[i]:i})
    return []