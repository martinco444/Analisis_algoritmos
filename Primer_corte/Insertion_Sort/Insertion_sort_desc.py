nums = [5, 7, 2, 4, 1, 6, 3, 10, 8, 9]
current = 0

for j in range(1, len(nums)):
    current = nums[j]
    i = j - 1
    while i >= 0 and nums[i]<current:
        nums[i + 1] = nums[i]
        i = i - 1
    nums[i + 1] = current
    
print(f"el array en orden descendente es: {nums}")
