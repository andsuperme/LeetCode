class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        left, right = 0, k - 1
        s_list = list(s)
        while left < right:
            temp = s_list[left]
            s_list[left] = s_list[right]
            s_list[right] = temp

            left += 1
            right -= 1
        return "".join(s_list)
