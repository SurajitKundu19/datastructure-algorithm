def partition(nums: list, start: int, end: int) -> int:
    pivot_index = 0
    pivot_value = nums[pivot_index]

    while start < end:
        while nums[start] < pivot_value:
            start += 1
        while nums[end] > pivot_value:
            end -= 1
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]

    nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
    print(nums)


def quicksort(nums: list, start: int, end: int):
    partition(nums, 1, len(nums) - 1)


if __name__ == "__main__":
    quicksort([11, 12, 4, 5, 29, 6, 18], 0, 5)
