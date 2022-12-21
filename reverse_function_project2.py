list1=[[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(x):
    x.reverse()
    for i in x:
        if type(i) == list:
            i.reverse()
reverse_list(list1)
print(list1)
            

