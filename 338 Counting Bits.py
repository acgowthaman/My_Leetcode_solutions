class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            count = 0
            j = i
            while j:
                count += j & 1
                j >>= 1
            ans.append(count)
        return ans
