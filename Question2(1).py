

def find_max(arr):
    if len(arr) == 0:
        return None  

    max_n = arr[0]  
    for n in arr[1:]:  
        if n > max_n:
            max_n = n

    return max_n

my_array = [20, 100, 90, 35, 66, 98, 11]

maximum = find_max(my_array)

print("The maximum number in the array is:", maximum)