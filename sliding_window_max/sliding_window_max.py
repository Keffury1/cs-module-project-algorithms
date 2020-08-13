'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# array for max numbers
# look at numbers in array by k
# pull out largest from each
# add to max numbers array
def sliding_window_max(nums, k):
    max_nums = []
    for num in range(len(nums)-k+1):
        max_nums.append(max(nums[num:num+k]))
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
