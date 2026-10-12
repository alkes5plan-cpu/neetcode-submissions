class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap= {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        return [item[0] for item in sorted(hashMap.items(), key=lambda x: x[1], reverse=True)[:k]]