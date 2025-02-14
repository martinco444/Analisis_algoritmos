
nums = [5, 7, 2, 4, 1, 6, 3, 10, 8, 9]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums

print("Array ordenado:", insertion_sort(nums))