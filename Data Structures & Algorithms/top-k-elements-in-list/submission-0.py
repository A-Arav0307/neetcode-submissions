class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums: 
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
            
        sorted_nums = sorted(nums_dict.items(), key=lambda x : x[1], reverse=True)
        print(sorted_nums)
        final_list = []
        for i in range(k): 
            final_list.append(sorted_nums[i][0])
            
        return final_list

