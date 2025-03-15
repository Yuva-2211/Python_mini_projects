def find_sum_pair(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == tar:
                return True
    return False

# Example usage
arr = [1, 2, 3, 4, 5, 6]
tar = 3
result = find_sum_pair(arr, tar)
print(result)