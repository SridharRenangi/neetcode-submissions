class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] =1
        
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        top_k = sorted_items[:k]

        result = []

        for item in top_k:
            result.append(item[0])    
        return result
        
