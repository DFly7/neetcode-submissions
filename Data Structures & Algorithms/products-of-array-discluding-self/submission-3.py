class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # in index i store product of index 0
        prefixSum = []
        currentSum = 1
        for n in nums:
            prefixSum.append(currentSum)
            currentSum *= n
        print(prefixSum)

        postfixSum = [1] * len(nums)
        currentSum = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixSum[i] = currentSum
            currentSum *= nums[i]

        
        out = []
        for i in range(len(nums)):
            out.append(prefixSum[i] * postfixSum[i])
        return out 

                




