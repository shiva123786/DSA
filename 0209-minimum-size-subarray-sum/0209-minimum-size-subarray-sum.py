class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        window_start = 0
        window_sum = 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            while window_sum >= target:
                min_length = min(min_length, window_end - window_start+1)
                window_sum -= nums[window_start]
                window_start += 1
        return min_length if min_length != math.inf else 0