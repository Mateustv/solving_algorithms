def groupAnagrams(strs):
    test_list = {}
    for i in strs:
        if ''.join(sorted(i)) in test_list:
            test_list[''.join(sorted(i))].append(i)
        else:
            test_list.update({''.join(sorted(i)):[i]})
    return test_list.values()