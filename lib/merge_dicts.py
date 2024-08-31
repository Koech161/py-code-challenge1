def merge_dicts (dict1,dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1    
dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}
dict3 = merge_dicts(dict1, dict2)
print(dict3)