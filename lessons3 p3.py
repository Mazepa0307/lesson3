def split_list(lst):
    if len(lst) ==0:
        return [[], []]

    if len(lst) % 2 ==0:
        list1 = lst[:len(lst)//2]
        list2 = lst[len(lst)//2:]
    else:
        list1 = lst[:len(lst)//2 + 1]
        list2 = lst[len(lst)//2 + 1:]

    return [list1, list2]
print(split_list([1,2,3,4,5,6]))
print(split_list([1,2,3]))
print(split_list([1,2,3,4,5]))
print(split_list([]))