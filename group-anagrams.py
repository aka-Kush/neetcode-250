class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        ans = []
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in my_map:
                my_map[sorted_str] = []
            my_map[sorted_str].append(s) 

        return list(my_map.values())
