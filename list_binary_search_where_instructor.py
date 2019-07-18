def list_binary_search_where(list,value,index=0):
    if len(list) == 0:
        return [False, None]

    elif len(list) == 1:
        if list[0] != value:
            return [False, None]
        else:
            return [True,index]

    else:
        if value < list[len(list)//2]:
            new_list = list[:len(list)//2]
            index=index+0

        else:
            new_list = list[len(list)//2:]
            index=index+len(list)//2

        return list_binary_search_where(new_list,value,index)
        
A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]

print list_binary_search_where(A,1,0)
print list_binary_search_where(A,2,0)
print list_binary_search_where(A,3,0)
print list_binary_search_where(A,9,0)
print list_binary_search_where(A,13,0)
print list_binary_search_where(A,24,0)
print list_binary_search_where(A,25,0)
print list_binary_search_where(A,26,0)
