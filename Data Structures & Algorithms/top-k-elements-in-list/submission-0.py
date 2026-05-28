class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##iterate through the entire array
        ##add one to the list per value you see the count the frequency
        res = []
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        print(count)

        for c in range(k):
            key = max(count, key=count.get)
            res.append(key)
            count.pop(key)
        return res
