# Ascending:- 
list = [3,32,23,12,45,24,56]
new_list=[]
while list:
    minimum = list[0]
    for x in list:
        if x < minimum:
            minimum=x
    new_list.append(minimum)
    list.remove(minimum)
print(new_list)

#Descending
list = [3,32,23,12,45,24,56]
new_list=[]
while list:
    minimum = list[0]
    for x in list:
        if x > minimum:
            minimum=x
    new_list.append(minimum)
    list.remove(minimum)
print(new_list)
