dict_test = {
    'Pi': 'Zhou Shuwen',
    'Alice': 'Lan',
    'Mo': 'Zhou Shuwen'
}


list_key = list(dict_test.keys())
list_val = list(dict_test.values())
new_dict = {}
new_dict = new_dict.fromkeys(list_val, [])
new_list_key = list(new_dict.keys())

for i in range(len(new_dict)):
    temp = []
    for j in range(len(dict_test)):
        if new_list_key[i] == dict_test[list_key[j]]:
            temp.append(list_key[j])

    # print(temp)
    new_dict[new_list_key[i]] = temp
    # print(new_dict)

print(new_dict)



















