class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # res = 0
        # for i, num_1 in enumerate(nums):
        #     for j in range(i+1, len(nums)):
        #         if num_1 + nums[j] < target:
        #             res += 1

        # return res

        nums.sort()
        res = 0
        left, right = 0, len(nums) - 1

        while left < right:
            pair_sum = nums[left] + nums[right]

            if pair_sum < target:
                res += right - left
                left += 1
            elif pair_sum > target:
                right -= 1
            else:
                right -= 1

        return res
