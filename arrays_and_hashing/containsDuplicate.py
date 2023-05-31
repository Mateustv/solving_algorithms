def containsDuplicate(nums):
    test_list = {}
    for i in nums:
        if i in test_list:
            return True
        else:
            test_list.update({i:1})
    return False