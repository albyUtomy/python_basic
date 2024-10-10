unordered_list = [2,3,4,2,3,5,1]

def bubble_sort():
    for i in range(0,len(unordered_list)):
        for j in range(0,len(unordered_list)-i-1):
            if unordered_list[j] > unordered_list[j+1]:
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]

    print("Bubble Sort : ",unordered_list)




# merge sort
def merge_sort(input_lst):
    if len(input_lst) > 1:
        mid = len(input_lst)//2

        left_half = input_lst[:mid]
        right_half = input_lst[mid:]

        # using recursive method
        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0

        while i< len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_lst[k] = left_half[i]
                i += 1
            else:
                input_lst[k] = right_half[j]
                j += 1
            k +=1

        while i<len(left_half):
            input_lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            input_lst[k] = right_half[j]
            j +=1
            k += 1

merge_sort(unordered_list)
print("Sorted Array : ", unordered_list)