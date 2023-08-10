#6.1
list1 = ["HDDDDDGGDi", "Good", "morning"]
newlist = []
for item in list1:
    upperChar = [x for x in item if x.isupper()]
    if len(upperChar) != 0:
        newlist.append(upperChar)
print(newlist)
