class Solution:
    def twoSum(self,nums,target): 
        visited={}
        for i in range(len(nums)):
            lists=target-nums[i]
            if lists in visited:
                return[visited[lists],i]
            visited[nums[i]]=i
        