def isAnagram(s, t):
  test_anagram = {}
  for i in s:
      if i in test_anagram:
          test_anagram[i] += 1
      else:
          test_anagram.update({i:1})
  for i in t:
      if i in test_anagram:
          test_anagram[i] -= 1
      else:
          test_anagram.update({i:1})
  for i in test_anagram:
      if test_anagram[i] != 0:
          return False
  return True  