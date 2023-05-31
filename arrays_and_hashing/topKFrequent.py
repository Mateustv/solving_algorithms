def topKFrequent(nums, k):
    test_list = {}
    for i in nums:
        if i in test_list:
            test_list[i] += 1
        else:
            test_list.update({i:1})
    return sorted(test_list, key=test_list.get, reverse=True)[:k]