def bubble_sort(nums: list):
    right_index = len(nums)
    while right_index > 0:
        for i in range(right_index - 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
        right_index -= 1
    return nums


def bubble_sort_keys(nums: list, key: str):
    right_index = len(nums)
    while right_index > 0:
        for i in range(right_index - 1):
            if nums[i][key] > nums[i + 1][key]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
        right_index -= 1
    return nums


if __name__ == "__main__":
    num_ls = [1, 6, 3, 9, 12, 1]
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
    ]
    print(bubble_sort(num_ls))
    print(bubble_sort_keys(elements, "transaction_amount"))
    print(bubble_sort_keys(elements, "name"))
