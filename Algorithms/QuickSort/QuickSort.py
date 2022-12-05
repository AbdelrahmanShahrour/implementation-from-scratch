def swap(my_list:list, index1:int, index2:int):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list:list, pivot_index:int, end_index:int) -> int:
    swap_index:int = pivot_index
                  # we don't wanna check same ele again
    for i in range(pivot_index + 1, end_index + 1): # we want to include the end one
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            # swapping i and swap index values
            swap(my_list, swap_index, i)

    # At end of for loop swap index will be a middle
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list:list, left:int, right:int):
    if left < right: # Base case
                                    # we do left + 1, right + 1 there
        pivot_index = pivot(my_list, left, right)
        # For left
        quick_sort_helper(my_list, left, pivot_index - 1) # As 4 is already sorted
        # For right
        quick_sort_helper(my_list, pivot_index + 1, right)

    return my_list

def quick_sort(my_list:list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)