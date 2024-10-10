unordered_list = [2,3,4,2,3,5,1]

def bubble_sort():
    for i in range(0,len(unordered_list)):
        for j in range(0,len(unordered_list)-i-1):
            if unordered_list[j] > unordered_list[j+1]:
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]

    print("Bubble Sort : ",unordered_list)

def merge_sort(input_lst):
    mid = len(unordered_list)//2

    left_half = unordered_list[:mid]
    right_half = unordered_list[mid:]

    # using recursive method
    merge_sort(left_half)
    merge_sort(right_half)

    i=j=k=0

    
