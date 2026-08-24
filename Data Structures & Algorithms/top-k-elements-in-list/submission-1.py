class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use a hashmap to keep track of ints
        #iterate through nums, if seen, plus one to the hash, if not, add
        #return k most
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        top_k = sorted(seen.keys(), key=lambda x: seen[x], reverse=True)[:k]
        return top_k