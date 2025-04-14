import numpy as np

def max_crossing_subarray(A, low, mid, high):
    # Implementación de max_crossing_subarray
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return [max_left, max_right, left_sum + right_sum]

def find_max_subarray(A, low, high):
    if high == low:
        return [low, high, A[low]]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        else:
            return [cross_low, cross_high, cross_sum]

if __name__ == '__main__':
    A = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    low = 0
    high = len(A) - 1
    
    (max_low, max_high, max_sum) = find_max_subarray(A, low, high)
    print("El subarreglo con la suma máxima es:", A[max_low:max_high+1])
    print("La suma máxima es:", max_sum)
