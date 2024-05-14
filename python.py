def findIndex(arr, num):
    indexes = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                indexes = [i, j]
                break
        if indexes:
            break
    if not indexes:
        indexes = [-1]
    return indexes


list = [2, 8, 8, 12, 15]
number = 16
print(findIndex(list, number))  
