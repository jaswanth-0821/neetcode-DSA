class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NA"
        if len(strs)==1:
            return strs[0]
        return "-><-".join(strs)
    def decode(self, s: str) -> List[str]:
        if s=="NA":
            return []
        return s.split("-><-")