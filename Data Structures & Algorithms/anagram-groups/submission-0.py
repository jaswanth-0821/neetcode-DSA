class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = [[0]*26 for _ in strs]

        for idx,i in enumerate(strs):
            for s in i:
                counts[idx][ord(s) - ord('a')] +=1
        return_values = []
        grouped_ids  = {}
        for idx, i in enumerate(counts):
            if tuple(i) not in grouped_ids:
                grouped_ids[tuple(i)] = [idx]
            else:
                grouped_ids[tuple(i)].append(idx)
        for key,values in grouped_ids.items():
            temp = []
            for v in values:
                temp.append(strs[v])
            return_values.append(temp)

        return return_values