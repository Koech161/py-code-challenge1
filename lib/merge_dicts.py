def merge_dicts (dict1,dict2):

    merged_dict = {}
    for key in dict1:
        if key in merged_dict:
            merged_dict[key] +=  dict1[key]
        else:
            merged_dict[key] = dict1[key]    

    for key in dict2:
        if key in merged_dict:
            merged_dict[key] += dict2[key]
        else: 
            merged_dict[key] = dict2[key]    

    return merged_dict

# dict1 = {'a': 10, 'b': 6}
# dict2 = {'b': 4, 'c': 6}
# merged_dict = merge_dicts(dict1, dict2)
# print(merged_dict)        