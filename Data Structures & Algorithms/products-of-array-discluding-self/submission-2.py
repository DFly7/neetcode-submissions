class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i, n in enumerate(nums):
            for j in range(len(output)):
                if i == j:
                    continue
                output[j] = output[j] * n
        return output

            