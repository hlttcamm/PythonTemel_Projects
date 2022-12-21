list1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
empty=[] 
def flatten(x):               
    for i in x:
        if not type(i)==list:
            empty.append(i)
        else:
            flatten(i)
    return empty
flatten(list1) 