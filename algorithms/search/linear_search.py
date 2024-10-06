index = 1


def LinearSearch(nums, target: int) -> bool:
    for num in nums:
        if num == target:
            return True
    index += 1
    return False


nums = [5, 2, 8, 3, 2, 9]
target = 2
print(LinearSearch(nums, target))
print(f'index of "{target}" is {index}')

