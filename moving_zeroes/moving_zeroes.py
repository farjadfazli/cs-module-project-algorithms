'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    index = len(arr) - 1
    num_zeros = 0
    while index >= 0:
        if arr[index] == 0:
            arr.pop(index)
            num_zeros += 1
            index -= 1
        else:
            index -= 1
    arr.extend([0] * num_zeros)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")