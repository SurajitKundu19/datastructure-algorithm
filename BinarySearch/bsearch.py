def binary_search(nums: list, number_to_find: int) -> int:
    left_index = 0
    right_index = len(nums) - 1
    out_idx = []
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = nums[mid_index]
        if number_to_find == mid_number:
            out_idx.append(mid_index)
            index_c = mid_index - 1
            while index_c >= 0 and nums[index_c] == mid_number:
                out_idx.append(index_c)
                index_c -= 1
            index_r = mid_index + 1
            while index_r <= right_index and nums[index_r] == mid_number:
                out_idx.append(index_r)
                index_r += 1
            return sorted(out_idx)
        if number_to_find < mid_number:
            right_index = mid_index - 1
        if number_to_find > mid_number:
            left_index = mid_index + 1

    return out_idx


def binary_search_recursive(
    nums: list, numb_to_find: int, left_index: int, right_index: int
) -> int:
    mid_index = (left_index + right_index) // 2
    mid_value = nums[mid_index]

    if mid_value == numb_to_find:
        return mid_index
    if numb_to_find < mid_value:
        right_index = mid_index - 1
    if numb_to_find > mid_value:
        left_index = mid_index + 1

    if left_index <= right_index:
        return binary_search_recursive(nums, numb_to_find, left_index, right_index)
    else:
        return -1


if __name__ == "__main__":
    num_list = [1, 1, 4, 6, 9, 10, 15, 15, 15, 17]
    idx = binary_search(num_list, 1)
    print(f"Found number at {idx}")
    idx = binary_search_recursive(num_list, 66, 0, len(num_list) - 1)
    print(f"Found number at {idx}")
