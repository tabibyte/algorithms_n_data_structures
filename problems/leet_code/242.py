def isAnagram(s: str, t: str) -> bool:
    hash_map1 = {}
    hash_map2 = {}

    for letter in s:
        if letter not in hash_map1:
            hash_map1[letter] = 0
        hash_map1[letter] += 1
    print(hash_map1)

    for letter in t:
        if letter not in hash_map2:
            hash_map2[letter] = 0
        hash_map2[letter] += 1
    print(hash_map2)

    if hash_map1 == hash_map2:
        return True
    else: 
        return False

s = "aacc"
t = "ccac"
isAnagram(s,t)