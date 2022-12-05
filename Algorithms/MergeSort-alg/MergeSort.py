def merge(list1:list, list2:list) -> list:
    combined:list = []
    # pointers
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list1):
        combined.append(list2[j])
        j += 1

    return combined


# using recursion
def merge_sort(my_list:list) -> list:
    if len(my_list) == 1: # Base case
        return my_list

    mid:int = len(my_list)//2 # for odd
    left:list = my_list[:mid]
    right:list = my_list[mid:]

    return merge(merge_sort(left), merge_sort(right))