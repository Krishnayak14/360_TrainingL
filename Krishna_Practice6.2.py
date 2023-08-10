#6.2
lst = ['Smit', 'CSE', 'Jaya', 'Networking', 'Rayyan', 'Operating System']
def convert(lst):
    res_dict = {}
    for i in range(0, len(lst), 2):
        res_dict[lst[i]] = lst[i + 1]
    return res_dict

print(convert(lst))
