class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        P = []
        sum_i = 0
        l = len(nums)
        for i in range(len(nums)):
            sum_i = sum_i + nums[i]
            P.append(sum_i)
        for i in range(len(nums)):
            if i == 0:
                if 0 == P[l-1] - nums[i]:
                    return i
            elif i == l - 1:
                if P[i-1] == 0:
                    return i
            else:
                if P[i-1] == P[l-1] - P[i-1] - nums[i]:
                    return i
        return -1
           
           
