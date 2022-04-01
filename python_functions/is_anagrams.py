def is_anagrams(s1,s2): # complexity O(n) 
    if len(s1) != len(s2):
        return False
    hash_array1 = hash(s1)
    hash_array2 = hash(s2)
    for key in hash_array1:
        if key not in hash_array2 or hash_array1[key] != hash_array2[key]:
            return False
    return True
def hash(s):
    dictionary={}
    for ch in s:
        if ch in dictionary:
            dictionary[ch] +=1
        else:
            dictionary[ch] = 1
    return dictionary

def is_anagrams2(s1,s2): # complexity O(nlog n) 
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

print(is_anagrams('aaa','aba'))
<<<<<<< HEAD:python_functions/is_anagrams.py
print(is_anagrams2('aaa','aba'))
=======
print(is_anagrams2('aaa','aba'))
>>>>>>> 6d913c1d6b4432cd21a35b56c0beba0791709216:functions/is_anagrams.py
