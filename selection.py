def selection(array,size):
    for i in range(size):
        mid_index=i
        for j in range(i+1,size):
            
            if arr[j]<array[mid_index]:
                mid_index=j
        array[i],array[mid_index]=array[mid_index],array[i]
arr=[9,8,7,6,5,4,3,2,1]
size=len(arr)
selection(arr, size)
print(arr)