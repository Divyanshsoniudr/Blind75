class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))  # Sort the characters of the string
            res[sorted_s].append(s)  # Append the string to the corresponding sorted key in the dictionary

        return list(res.values())
