'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    if not nums or k < 1 or k > len(nums):
        return []
    answer = []
    dequeue = []
    for i, num in enumerate(nums):
        if dequeue and dequeue[0] < i - k + 1:
            dequeue.pop(0)
        while dequeue and nums[dequeue[-1]] < num:
            dequeue.pop()
        dequeue.append(i)
        if i >= k - 1:
            answer.append(nums[dequeue[0]])

    return answer


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
