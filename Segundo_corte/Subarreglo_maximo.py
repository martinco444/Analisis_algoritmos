import numpy as np

def max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return [max_left, max_right, left_sum + right_sum]

if __name__ == '__main__':
    A = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    low = 0
    mid = len(A) // 2
    high = len(A) - 1
    
    result = max_crossing_subarray(A, low, mid, high)
    print(result)